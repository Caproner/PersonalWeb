function rsa(password){
    var pub_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCwKtpAUURVyqiuQvq4P7rD/6lK/wZxNFtkyR+gNEM3X7r79n0GxzR7ePaBU6sW0A/eLfAF4ePxRfKzxW7t9cfblXyEFIsxHWwbu5m3oBSYFP0d70s5asdqf+caXYoqACXOm336QVOd7O3Oz3Gwfvq7uhfSJ8NdyjG9o6VPvoUXFwIDAQAB";
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(pub_key);
    return encrypt.encrypt(password);
}

function rsa_password(password){
    if(password.length > 19){
        password = '1234567890123456789';
    }
    password = rsa(password);
    return password;
}

function login_crypt(){
    var password = rsa_password($('#id_password').val());
    $('#id_password').val(password);
    return true;
}

function register_crypt(){
    var password1 = rsa_passworda($('#id_password1').val());
    $('#id_password1').val(password1);
    var password2 = rsa_password($('#id_password2').val());
    $('#id_password2').val(password2);
    return true;
}