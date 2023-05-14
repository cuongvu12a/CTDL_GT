(() => {
  const input = [10, 17, 27, 15, 29, 21, 11, 14, 18, 12, 17, 17];
  main(input);
})();

function main(input) {
  const result = mergeSort(input);
  console.log(result);
}

function mergeSort(arr) {
  if (arr.length === 1) return arr;
  const index = Math.floor((0 + arr.length) / 2);
  const leftArr = mergeSort(arr.slice(0, index));
  const rightArr = mergeSort(arr.slice(index, arr.length));

  return merge(leftArr, rightArr);
}

function merge(firstArr, secondArr) {
  let firstIdx = 0;
  let secondIdx = 0;
  const result = [];
  while (firstIdx < firstArr.length && secondIdx < secondArr.length) {
    if (firstArr[firstIdx] < secondArr[secondIdx]) {
      result.push(firstArr[firstIdx]);
      firstIdx += 1;
    } else {
      result.push(secondArr[secondIdx]);
      secondIdx += 1;
    }
  }

  while (firstIdx < firstArr.length) {
    result.push(firstArr[firstIdx]);
    firstIdx += 1;
  }

  while (secondIdx < secondArr.length) {
    result.push(secondArr[secondIdx]);
    secondIdx += 1;
  }

  return result;
}
