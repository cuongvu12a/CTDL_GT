using StackExchange.Redis;
using Npgsql;
using System.Text.Json;

var redisHost = Environment.GetEnvironmentVariable("REDIS_HOST") ?? "redis";
var pgHost = Environment.GetEnvironmentVariable("POSTGRES_HOST") ?? "db";
var pgUser = Environment.GetEnvironmentVariable("POSTGRES_USER") ?? "postgres";
var pgPassword = Environment.GetEnvironmentVariable("POSTGRES_PASSWORD") ?? "postgres";
var pgDb = Environment.GetEnvironmentVariable("POSTGRES_DB") ?? "votes";

var connString = $"Host={pgHost};Username={pgUser};Password={pgPassword};Database={pgDb}";

// Tao bang neu chua ton tai
await using (var conn = new NpgsqlConnection(connString))
{
    await conn.OpenAsync();
    var cmd = new NpgsqlCommand(
        "CREATE TABLE IF NOT EXISTS votes (id VARCHAR(255) NOT NULL UNIQUE, vote VARCHAR(255) NOT NULL)",
        conn);
    await cmd.ExecuteNonQueryAsync();
    Console.WriteLine("Database table ready.");
}

// Ket noi Redis
var redis = await ConnectionMultiplexer.ConnectAsync(redisHost);
var db = redis.GetDatabase();

Console.WriteLine("Worker started. Waiting for votes...");

while (true)
{
    var value = await db.ListLeftPopAsync("votes");
    if (value.HasValue)
    {
        try
        {
            var voteData = JsonSerializer.Deserialize<VoteData>(value.ToString());
            if (voteData?.voter_id != null && voteData?.vote != null)
            {
                await using var conn = new NpgsqlConnection(connString);
                await conn.OpenAsync();
                var cmd = new NpgsqlCommand(
                    "INSERT INTO votes (id, vote) VALUES (@id, @vote) ON CONFLICT (id) DO UPDATE SET vote = @vote",
                    conn);
                cmd.Parameters.AddWithValue("id", voteData.voter_id);
                cmd.Parameters.AddWithValue("vote", voteData.vote);
                await cmd.ExecuteNonQueryAsync();
                Console.WriteLine($"Vote saved: {voteData.voter_id} -> {voteData.vote}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error processing vote: {ex.Message}");
        }
    }
    else
    {
        await Task.Delay(100);
    }
}

record VoteData(string? voter_id, string? vote);
