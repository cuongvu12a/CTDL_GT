(() => {
  // const input = [1, 4, 1, 2, 7, 5, 2];
  const input = [0, 2, 1, 17, 17, 2, 4, 3, 2, 3, 1, 4, 5, 9, 11, 12, 0];
  main(input);
})();

function main(input) {
  const results = countingSort(input);
  console.log(results);
}

function countingSort(input) {
  const counters = [0];
  const results = [];

  for (const value of input) {
    counters[value] = (counters[value] ?? 0) + 1;
  }

  console.log("Step 1:", { counters });

  for (let index = 1; index < counters.length; index += 1) {
    counters[index] = (counters[index - 1] || 0) + (counters[index] || 0);
  }

  console.log("Step 2:", { counters });

  const placeOfValue = [0, ...counters];

  console.log("Step 3:", { placeOfValue });

  for (const value of input) {
    results[placeOfValue[value]] = value;
    placeOfValue[value] += 1;
  }

  return results;
}
