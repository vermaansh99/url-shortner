db = [ {
    "shortcode":"ABC",
    "url":"https://chat.openai.com/c/5e61208b-3527-41a5-9cbe-7eb61e07371b"
}]



index = db.findIndex((item)=>item["shortcode"]==="ABC")

let item = db[index]


let short_url = "http://localhost:8080/"+item["shortcode"]
console.log(short_url)

let short_code = "ABC"

let INDEX = db.findIndex((i)=>i["shortcode"]===short_code)

console.log(INDEX)
let url = db[INDEX]["url"]

console.log(url)

