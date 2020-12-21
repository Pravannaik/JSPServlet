var http = require('http');
var fs = require('fs');
var requests = require('requests');

var readFile = fs.readFileSync('home.html', 'utf8');

const replaceVal = (tempVal, orgVal) => {
    let temperature = tempVal.replace("{%tempValue%}", orgVal.main.temp);
    temperature = temperature.replace("{%tempMin%}", orgVal.main.temp_min);
    temperature = temperature.replace("{%tempMax%}", orgVal.main.temp_max);
    temperature = temperature.replace("{%city%}", orgVal.name);
    temperature = temperature.replace("{%country%}", orgVal.sys.country);
    return temperature;
}


const server = http.createServer((req, res) => {
    if(req.url == '/'){
        requests('http://api.openweathermap.org/data/2.5/weather?q=Panjim&appid=d8f408c5029007f37b9106eaeb709d76')
        .on('data', (chunk) => {
            const objData = JSON.parse(chunk);
            const arrObj = [objData];
            //console.log(chunk)
            const realTimeData = arrObj.map(val => replaceVal(readFile, val)).join(""); //to convert in string 
            //because, if we dont put .join('') we will get output in array
            res.write(realTimeData);
            //console.log(realTimeData);
        })
        .on('end', (err) => {
            if (err) return console.log('connection closed due to errors', err);
                //console.log('end');
                res.end();
        });
    }else{
        res.end("Not Found");
    }
})

server.listen(3000);
console.log("Listenning");


//This is alternate way of doing

// var server = http.createServer((req, res) => {
//     res.writeHead(200, {'content-type' : 'text/html'});
//     fs.createReadStream(__dirname + '/home.html').pipe(res);
// });

// server.listen(3000);
// console.log("Listenning");
