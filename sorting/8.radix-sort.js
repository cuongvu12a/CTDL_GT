(() => {
  const input = [170, 45, 75, 90, 802, 24, 2, 66];

  main(input);
})();

function main(input) {
  const max = Math.max(...input);
  let result = [...input];
  for (let radix = 1; Math.floor(max / radix) > 0; radix *= 10) {
    result = countingSort(result, radix);
    console.log(result);
  }
}

function countingSort(input, radix) {
  const counters = [0];
  const results = [];

  for (const value of input) {
    counters[withRadix(value, radix)] =
      (counters[withRadix(value, radix)] ?? 0) + 1;
  }

  for (let index = 1; index < counters.length; index += 1) {
    counters[index] = (counters[index - 1] || 0) + (counters[index] || 0);
  }

  const placeOfValue = [0, ...counters];
  for (const value of input) {
    results[placeOfValue[withRadix(value, radix)]] = value;
    placeOfValue[withRadix(value, radix)] += 1;
  }
  // const placeOfValue = [...counters];
  // for (const value of input) {
  //   results[placeOfValue[withRadix(value, radix)] - 1] = value;
  //   placeOfValue[withRadix(value, radix)] -= 1;
  // }

  return results;
}

function withRadix(number, radix) {
  return Math.floor(number / radix) % 10 || 0;
}
