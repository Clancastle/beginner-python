const form = document.getElementById('form');
const email = document.getElementById('email');
const fname = document.getElementById('fname');
const age = document.getElementById('age');

document.getElementById('form').addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();
});

const setError = (element, message) => {
    const cntrl = element.parentElement;
    const errorDisplay = cntrl.querySelector('.error');

    errorDisplay.innerText = message;
    cntrl.classList.add('error');
    cntrl.classList.remove('success');
};

const setSuccess = element => {
    const cntrl = element.parentElement;
    const errorDisplay = cntrl.querySelector('.error');

    errorDisplay.innerText = '';
    cntrl.classList.add('success');
    cntrl.classList.remove('error');
};
const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    return re.test(String(email).toLowerCase());
}
const validateInputs = () => {
    const emailValue = email.value.trim();
    const ageValue = age.value.trim();
    const fnameValue = fname.value.trim();

    if(email === ""){
        setError(email, "Email is required")

    }else if(!isValidEmail(email)){
        setError(email, "Invalid Email")
    }else {
        setSuccess(email)
    }
// let regexAge=/^[0-9]+$/
    if (age !== 34){
        setError(age, "Age ")
    }else{
        setSuccess(age)
    }
};