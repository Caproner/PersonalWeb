function password_sha256(password_id){
    var x = $('#' + password_id).text();
    alert(x);
}

function login_sha256(){
    alert('ready');
    password_sha256('id_password');
}