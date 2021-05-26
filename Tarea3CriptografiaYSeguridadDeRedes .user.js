// ==UserScript==
// @name         Tarea3CriptografiaYSeguridadDeRedes
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Encriptación con crypto-js
// @author       Juan José Vergara
// @match        https://jjvergaramanzi.github.io/Tarea3CriptoYSegRedes/
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js
// ==/UserScript==

(function() {
    //Capturar las variables del html
    var AEShtml = document.getElementsByClassName("AES");
    var IVhtml = document.getElementsByClassName("iv");
    var Keyhtml = document.getElementsByClassName("keys");

    //Parseo de IV y Key
    var IVParsed= CryptoJS.enc.Hex.parse(IVhtml[0].id);
    var KeyParsed =CryptoJS.enc.Hex.parse(Keyhtml[0].id);
    var cipher = CryptoJS.lib.CipherParams.create({
            ciphertext: CryptoJS.enc.Base64.parse(AEShtml[0].id)
        });
    //Desencriptacion
    var decrypted = CryptoJS.AES.decrypt(cipher, KeyParsed,{
        iv: IVParsed,
        mode: CryptoJS.mode.CFB,
        padding: CryptoJS.pad.ZeroPadding
    });
    alert(decrypted.toString(CryptoJS.enc.Utf8));
})();