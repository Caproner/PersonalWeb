function rsa(password){
    var pub_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCwKtpAUURVyqiuQvq4P7rD/6lK/wZxNFtkyR+gNEM3X7r79n0GxzR7ePaBU6sW0A/eLfAF4ePxRfKzxW7t9cfblXyEFIsxHWwbu5m3oBSYFP0d70s5asdqf+caXYoqACXOm336QVOd7O3Oz3Gwfvq7uhfSJ8NdyjG9o6VPvoUXFwIDAQAB";
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(pub_key);
    return encrypt.encrypt(password);
}

function login_crypt(){
    var password = rsa($('#id_password').val());
    $('#id_password').val(password);
    alert($('#id_password').val());
    return true;
}