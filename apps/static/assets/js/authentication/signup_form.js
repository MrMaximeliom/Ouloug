import {handle_input_errors,check_empty_input,check_input_syntax,check_password_policy,check_passwords_match} from './handle_forms.js';
const page_document = document;
const normal_chars_regex = /^[a-zA-Z\s]+$/g;
const email_regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/g;
const phone_number_regex = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{3,4}$/gim;
const password_special_regex = /\W{1,}/g;
const password_numbers_regex = /[0-9]{2,}/g;
const password_capital_letter_regex = /[A-Z]{1,}/g
const username_regex = /^[a-z0-9_-]{6,10}$/g

page_document.addEventListener("DOMContentLoaded",()=>{
const error_messages = JSON.parse(page_document.getElementById('my-data').innerHTML);


let sign_up_form = document.getElementById("signUpForm");
// first name checks
// check input for first name field
page_document.getElementById("id_first_name").addEventListener("input",(e)=>{
check_empty_input("first_name_error","id_first_name",error_messages.first_name_empty_error);
});
// check input for first name field while changing
page_document.getElementById("id_first_name").addEventListener("change",(e)=>{
check_input_syntax("first_name_error","id_first_name",normal_chars_regex,error_messages.first_name_error);
})
// second name checks
// check input for second name field
page_document.getElementById("id_second_name").addEventListener("input",(e)=>{
check_empty_input("second_name_error","id_second_name",error_messages.second_name_empty_error);
});
// check input for second name field while changing
page_document.getElementById("id_second_name").addEventListener("change",(e)=>{
check_input_syntax("second_name_error","id_second_name",normal_chars_regex,error_messages.second_name_error);
})
// third name checks
// check input for third name field
page_document.getElementById("id_third_name").addEventListener("input",(e)=>{
check_empty_input("third_name_error","id_third_name",error_messages.third_name_empty_error);
});
// check input for third name field while changing
page_document.getElementById("id_third_name").addEventListener("change",(e)=>{
check_input_syntax("third_name_error","id_third_name",normal_chars_regex,error_messages.third_name_error);
})
// fourth name checks
// check input for fourth name field
page_document.getElementById("id_fourth_name").addEventListener("input",(e)=>{
check_empty_input("fourth_name_error","id_fourth_name",error_messages.fourth_name_empty_error);
});
// check input for fourth name field while changing
page_document.getElementById("id_fourth_name").addEventListener("change",(e)=>{
check_input_syntax("fourth_name_error","id_fourth_name",normal_chars_regex,error_messages.fourth_name_error);
})
// phone number checks
// check input for phone number field
page_document.getElementById("id_phone_number").addEventListener("input",(e)=>{
check_empty_input("phone_number_error","id_phone_number",error_messages.phone_number_empty_error);
});
// check input for phone number field while changing
page_document.getElementById("id_phone_number").addEventListener("change",(e)=>{
check_input_syntax("phone_number_error","id_phone_number",phone_number_regex,error_messages.phone_number_error);
});
// username checks
// check input for username field
page_document.getElementById("id_username").addEventListener("input",(e)=>{
check_empty_input("username_error","id_username",error_messages.username_empty_error);
});
// check input for username field while changing
page_document.getElementById("id_username").addEventListener("change",(e)=>{
check_input_syntax("username_error","id_username",username_regex,error_messages.username_error);
});
//// password check
//// check input for password field
//page_document.getElementById("id_password").addEventListener("input",(e)=>{
//check_empty_input("password_error","id_password",error_messages.password_empty_error);
//});
//// confirm password check
//// check input for confirm password field
//page_document.getElementById("id_password2").addEventListener("input",(e)=>{
//check_empty_input("confirm_password_error","id_password2",error_messages.confirm_password_empty_error);
//});
// make confirm password enabled after entering password
page_document.getElementById("id_password").addEventListener("input",(e)=>{
let confirm_password = page_document.getElementById("id_password2");
confirm_password.removeAttribute("disabled");
});

// check passwords are match
page_document.getElementById("id_password2").addEventListener("input",(e)=>{
check_passwords_match("id_password","id_password2","confirm_password_error",error_messages.passwords_not_match)
});
// recheck passwords if user changed password
page_document.getElementById("id_password").addEventListener("change",(e)=>{
let confirm_password = page_document.getElementById("id_password2");
if(confirm_password.value !== "" && typeof confirm_password.value != "undefined" )
{
check_passwords_match("id_password","id_password2","confirm_password_error",error_messages.passwords_not_match)

}
});
// email checks
// check input for email field
page_document.getElementById("id_email").addEventListener("input",(e)=>{
check_empty_input("email_error","id_email",error_messages.email_empty_error);
});
// check input for email field while changing
page_document.getElementById("id_email").addEventListener("change",(e)=>{

check_input_syntax("email_error","id_email",email_regex,error_messages.email_error);
})
// handle registration form when submitted and
// check to see if there was no errors

function check_form_validation(){
let span_fields = sign_up_form.querySelectorAll("span");
let is_form_valid = false;
for(var field in span_fields){
if(span_fields[field].innerHTML === "" || typeof span_fields[field].innerHTML  === "undefined"){


is_form_valid = true;

}
else{
is_form_valid = false;
break;
}
}
return is_form_valid;
}
page_document.getElementById("signUpForm").addEventListener("submit",(e) => {
let is_form_valid = check_form_validation();
if(!is_form_valid){
e.preventDefault();
}

});








})