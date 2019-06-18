function password_sha256(password_id){
    var x = $('#' + password_id).val();
    alert(x);
}

function login_sha256(){
    alert('ready');
    password_sha256('id_password');
    return false;
}