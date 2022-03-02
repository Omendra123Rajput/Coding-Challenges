// Counting the Vowels in a String of Text
function countTheVowel ( str )
{
    let count = 0
    let newArray = str.toLowerCase().split( '' )
    console.log(newArray.length);
    for ( let i = 0; i < newArray.length; i++)
    {
        if (newArray[i]==='a' || newArray[i]==='e' || newArray[i]==='i' || newArray[i]==='o' || newArray[i]==='u')
        {
            count++
        }
        
    }
    return count
}

console.log(countTheVowel('hello hOW ARE You'));
    
    
    
  