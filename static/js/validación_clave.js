const forma = document.getElementById('formul');
const email = document.getElementById('correo');
const clave = document.getElementById('contraseña');
const clave2 = document.getElementById('contra2');
let toggleBtn = document.getElementById('toggleBtn');
let toggleBtn1 = document.getElementById('toggleBtn1');

let lowerCase = document.getElementById('lower');
let upperCase = document.getElementById('upper');
let digit = document.getElementById('number');
let specialChar = document.getElementById('special');
let minLength = document.getElementById('length');

document.querySelector('#contraseña').addEventListener('keyup', function () {
    checkPassword(this.value)
});


//Mostrar y ocultar clave

toggleBtn.onclick = function () {
    if (clave.type === 'password') {
        clave.setAttribute('type', 'text');
        toggleBtn.classList.add('hide');
    } else {
        clave.setAttribute('type', 'password');
        toggleBtn.classList.remove('hide');

    }
};

toggleBtn1.onclick = function () {
    if (clave2.type === 'password') {
        clave2.setAttribute('type', 'text')
        toggleBtn1.classList.add('mostrar');
    } else {
        clave2.setAttribute('type', 'password')
        toggleBtn1.classList.remove('mostrar');
    }
};


forma.addEventListener('submit', e => {
    e.preventDefault();
    validateInputs();
});


const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error')

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
};

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');

};

const isValidEmail = email => {
    const re = /^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$/
    return re.test(String(email).toLowerCase());
};


const validateInputs = () => {
    const emailValue = email.value.trim();
    const passwordValue = clave.value.trim();
    const password2Value = clave2.value.trim();


    if (!isValidEmail(emailValue)) {
        setError(email, 'Proporcionar un email válido.');
    } else {
        setSuccess(email);
    }

    if (password2Value !== passwordValue) {
        setError(clave2, 'Las claves no coinciden.');
    } else {
        setSuccess(clave2);
    }

    const allInputsValid = document.querySelectorAll('.valid').length === 5;
    if (allInputsValid) {
        document.querySelector("form").submit();
    } else {
        Swal.fire({
            icon: 'error',
            title: 'La clave debe contener al menos una letra mayúscula, una letra minúscula, ' +
                'un número, un carácter especial y tener una longitud mínima de 10 caracteres.',
            allowOutsideClick: true,
            showLoaderOnConfirm: true,
            preConfirm: () => {
                return new Promise((resolve) => {
                    setTimeout(() => {
                        resolve()
                    }, 700)
                })
            }
        })
    }
};


function checkPassword(data) {
    const lower = new RegExp('(?=.*[a-z])');
    const upper = new RegExp('(?=.*[A-Z])');
    const number = new RegExp('(?=.*[0-9])');
    const special = new RegExp('(?=.*[!@#\$%\^&\*])');
    const length = new RegExp('(?=.{10,})');

    //Validar minúsculas
    if (lower.test(data)) {
        lowerCase.classList.add('valid');
    } else {
        lowerCase.classList.remove('valid');
    }
    //Validar Mayúsculas
    if (upper.test(data)) {
        upperCase.classList.add('valid');
    } else {
        upperCase.classList.remove('valid');
    }

    // Validar números
    if (number.test(data)) {
        digit.classList.add('valid');
    } else {
        digit.classList.remove('valid');
    }

    //Validar caracteres especiales
    if (special.test(data)) {
        specialChar.classList.add('valid');
    } else {
        specialChar.classList.remove('valid');
    }
    //Mínimo de caracteres
    if (length.test(data)) {
        minLength.classList.add('valid');
    } else {
        minLength.classList.remove('valid');
    }
}