//sort array in decreasing Order
let arr = [5, 2, 1, -10, 8]


function sortArray(arr){
    arr.sort((a,b)=>a-b)
    arr.reverse()
}
sortArray(arr)


alert( arr )
