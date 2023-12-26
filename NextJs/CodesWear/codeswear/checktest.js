const checksum_lib = require('paytmchecksum')

var paytmChecksum = ""
var paytmParams = {}

const received_data = JSON.parse('{}');
for (var key in received_data){
    if(key == 'CHECKSUMHASH'){
        paytmChecksum = received_data
    }
    else{
        paytmParams[key] = received_data[key]
    }
}

var isValidChecksum = checksum_lib.verifySignature(paytmParams,"",paytmChecksum);
if(isValidChecksum){
    console.log('checksum matched')
}else{
    console.log("checksum mismatched")
}
