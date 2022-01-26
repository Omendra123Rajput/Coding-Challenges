//Write a function filterRangeInPlace(arr, a, b) that gets an array arr and removes from it all values except those that are between a and b. The test is: a ≤ arr[i] ≤ b.

let newNew = [5,3,8,1,2,1,3]

function filterRangeInPlace(arr,a,b){
    
    for( let i = 0 ; i<arr.length ; i++){

        if(  !(arr[i] >= a && arr[i] <= b) ){ //this checks whether the element is in the range or not.
            //if element is not in the range then we proceed


            let index = arr.indexOf(arr[i]) //find the index of the element

            arr.splice(index,1) //remove that element using index
            
        }

    }


}


filterRangeInPlace(newNew,1,4)

console.log(newNew)