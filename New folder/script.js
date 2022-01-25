// Write the function camelize(str) that changes dash-separated words like “my-short-string” into camel-cased “myShortString”.


function camelize(str){
    let arrOfStr = str.split('-') //splitting the array on the basis of '-' , [background,color,is,blue]
    let capitalLetter = [arrOfStr[0]] // new array [background]
    for(let i = 1 ; i<arrOfStr.length ; i++){
        // here we are making 1st letter of each Capital
        let slicedWord = arrOfStr[i].slice(0,1).toUpperCase() + arrOfStr[i].slice(1,)
        capitalLetter.push(slicedWord)
    }
    //[background,Color,Is,Blue]

    let result = capitalLetter.join('')
    console.log(result)

}


camelize("-backround-color-is-blue")