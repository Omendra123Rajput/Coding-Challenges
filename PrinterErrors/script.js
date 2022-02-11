function printerErrors(str)
{
        //creating a set of unwanted letters

        let newString = ['n','o','p','q','r','s','t','u','v','w','x','y','z']
    
        let count = 0


        //splitting the string and storing inthe array
        let arrayOfString = str.split('')


        //iterating and checking if the word from the string array is in unwanted array if yes the increasing the count
        arrayOfString.forEach( word => {
    
            if(newString.includes(word)){
    
                count+=1
    
            }
    
            
        })
    
        return `"${count}/${str.length}"` //returning the result
    
}

    
console.log(printerErrors("aaaxbbbbyyhwawiwjjjwwm"))
    
