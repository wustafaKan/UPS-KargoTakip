const express = require('express');
const app = express();
const port = 3000;


function createToken() {
    const $zoho_ =[
        "app",
        "ក",
        "ខ",
        "គ"
    ]
    
    var be = (new TextEncoder).encode([$zoho_[1], Date.now(), $zoho_[3]]);
    be[1] = 150,
    be[be.length - 2] = 150
    console.log(be);
    return "".concat(be)
    
}

app.listen(port, () => {
    console.log(`Açık: ${port}`);
});
app.get('/', (req, res) => {
    console.log("Token Oluşturuldu");
    
    res.send(createToken());
    
});

