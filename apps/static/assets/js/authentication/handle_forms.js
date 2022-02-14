const handle_input_errors = (span_id,input_id,text_state,error_message) =>{
document.getElementById(input_id).dataset.state = text_state;
document.getElementById(span_id).innerHTML = error_message;
}
const check_empty_input = (span_id,input_id,error_message) =>{
const value = document.getElementById(input_id).value;
if (!value)
{    document.getElementById(input_id).dataset.state = ''
   return  }
let trimmed = value.trim();
if (trimmed)
{
handle_input_errors(span_id,input_id,"valid","");
}
else
{
handle_input_errors(span_id,input_id,"invalid",error_message);
 }
}
const check_input_syntax = (span_id,input_id,regex,error_message)=>{
let value = document.getElementById(input_id).value.trim();
let evaluate = value.match(regex);
if(evaluate)
{
handle_input_errors(span_id,input_id,"valid","");
}
else{
handle_input_errors(span_id,input_id,"invalid",error_message);
}


}
const check_password_policy = (password_id)=>{
let password = document.getElementById(password_id).value;
let has_errors = false;
// check if password has at least one special character
if(special_letters_in_password){
// make the password's policy of containing at least one special character valid
document.getElementById("password-special").dataset.state = "valid";
has_errors = false;
}
else{
// make the password's policy of containing at least one special character invalid
document.getElementById("password-special").dataset.state = "invalid";
has_errors = true;
}
// check if password has at least two numbers
if(numbers_in_password){
// make the password's policy of containing at least two numbers valid
document.getElementById("password-number").dataset.state = "valid";
has_errors = false;
}
else{
// make the password's policy of containing at least two numbers character invalid
document.getElementById("password-number").dataset.state = "invalid";
has_errors = true;
}
// check if password has at least one capital letter
if(capital_letters_in_password){
// make the password's policy of containing at least one capital letter valid
document.getElementById("password-capital").dataset.state = "valid";
has_errors = false;
}
else{
// make the password's policy of containing at least one capital letter invalid
document.getElementById("password-capital").dataset.state = "invalid";
has_errors = true;

}
// check if password's length is at least 10 letters
if(password.length >= 8){
// make the password's policy of length valid
document.getElementById("password-length").dataset.state = "valid";
has_errors = false;
}
else{
// make the password's policy of length invalid
document.getElementById("password-length").dataset.state = "invalid";
has_errors = true;

}
// check if password not similar to users' full name


}
const check_passwords_match = (password_id,confirm_password_id,span_id,error_message)=>{
let password = document.getElementById(password_id).value;
let password2 = document.getElementById(confirm_password_id).value;
if(password === password2){
document.getElementById(span_id).innerHTML = '';
document.getElementById(confirm_password_id).dataset.state = "valid";
}
else{
document.getElementById(span_id).innerHTML = error_message;
document.getElementById(confirm_password_id).dataset.state = "invalid";

}
}
export {handle_input_errors,check_empty_input,check_input_syntax,check_password_policy,check_passwords_match};

