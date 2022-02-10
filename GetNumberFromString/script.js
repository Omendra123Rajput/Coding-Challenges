// Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56

function getNumberFromString(str){




    //remove the space btw words
    
    str = str.replaceAll(' ','')
    
    
    //split string and store in array
    
    let newStr = str.split('')
    
    console.log(newStr)
    //iterate overe the array , check for the typye of the letter
    let word = ''
    newStr.forEach( item=> {
    
        if(  isNaN(item) === false  ){
    
            word =  word+item
            
        }
    
        
    })
    
    
    
    
    
    //parse the number from the string
    console.log(parseInt(word))
    
    
}
    
getNumberFromString('hello12 how213')