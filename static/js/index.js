const input = document.getElementById('quantity');
const form = document.getElementById('form');
const errorElement = document.getElementById('error')


form.addEventListener('submit' , (e) => {
    let messages = []
    if (input.value == '' || input.value == null){
        messages.push('El campo es requerido')
    }

    if (!isNaN(input)){
        messages.push('El campo debe ser un numero')
    }

    if (messages.length > 0){
        e.preventDefault()
        errorElement.innerText = messages.join(', ')
    }
})


input.setAttribute('required', '');