
const string        = "AACAPwAAAEAAAEBAAACAQAAAoEA="
const binaryStr     = atob(string)
const len           = binaryStr.length

const bytes         = new Uint8Array(len) 
for(let i = 0; i < len; i++) {
    bytes[i] = binaryStr.charCodeAt(i)
}

const floatArray    = new Float32Array(bytes.buffer)

console.log(floatArray) 
