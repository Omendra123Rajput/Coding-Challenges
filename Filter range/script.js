// Write a function filterRange(arr, a, b) that gets an array arr, looks for
// elements with values higher or equal to a and lower or equal to b and
// return a result as an array.


function filterRange(arr,a,b){

    // let newArr = []

    // for ( let i = 0; i<arr.length ; i++){
    //     if(  arr[i] >= a && arr[i] <= b ){
    //         newArr.push(arr[i])

    //     }
    // }

    // return newArr



    let result = arr.filter(  

        (item) => (item >=a && item <=b) //filter iterate through all elements and returns array of filtered elements

    )

    return result

}

let newNew = [5,3,8,1,2,1,3]
console.log(filterRange(newNew,1,4) )