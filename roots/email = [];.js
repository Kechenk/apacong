email = [];
function readBody(xhr) {
    var data;
    if (!xhr.responseType || xhr.responseType === "text") {
        data = xhr.responseText;
    } else if (xhr.responseType === "document") {
        data = xhr.responseXML;
    } else {
        data = xhr.response;
    }
    return data;
}

function getEmail(page){
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
        data = readBody(xhr);
    }
}
xhr.open('GET', '/CMD_EMAIL_POP?json=yes&domain=ourdesa.my.id&page='+page+'&ipp=1000&bytes=yes', true);
xhr.send(null);
return data;
}

for (let i = 1; i < 18; i++){
    (function(i){
        setTimeout(function(){data = getEmail(i);
        data = JSON.parse(data);
        data = data.emails;
        for (let j = 0; j < 1000; j++){
            email.push(data[j]['login']);
        }
        }, 5000 * i);
    }(i));
}

let csvContent = "data:text/csv;charset=utf-8,";

email.forEach(function(rowArray) {
    let row = rowArray.toString();
    csvContent += row + "\r\n";
});