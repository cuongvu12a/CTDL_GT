(() => {
  const input = [10, 17, 27, 15, 29, 21, 11, 14, 18, 12, 17, 17];
  main(input);
})();

function main(input) {
  quickSort(input, 0, input.length - 1);
  console.log(input);
}

function quickSort(arr, low, hight) {
  if (low < hight) {
    const pi = partition(arr, low, hight);
    quickSort(arr, low, pi - 1);
    quickSort(arr, pi + 1, hight);
  }
}
function partition(arr, low, hight) {
  const pivot = arr[hight];
  let index = low;
  for (let cursor = low; cursor < hight; cursor += 1) {
    if (arr[cursor] < pivot) {
      swap(arr, index, cursor);
      index += 1;
    }
  }
  swap(arr, index, hight);
  return index;
}

function swap(arr, leftIdx, rightIdx) {
  const temp = arr[leftIdx];
  arr[leftIdx] = arr[rightIdx];
  arr[rightIdx] = temp;
}
