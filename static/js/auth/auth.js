document.querySelector('form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    console.log(new URLSearchParams(formData).toString());
    

    try {
        const response = await fetch('http://127.0.0.1:8000/auth/jwt/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded' // Устанавливаем правильный Content-Type
            },
            body: new URLSearchParams(formData).toString() // Преобразуем FormData в строку x-www-form-urlencoded
        });
        if (response.ok) {
            console.log(response.blob());
            localStorage.setItem('jwtToken', new URLSearchParams(formData).toString());
            window.location.href = '/';
        } else {
            // Если ответ не успешный, обрабатываем ошибку
            console.error('Ошибка при отправке данных:', response.status);
        }
    } catch (error) {
        console.error('Ошибка:', error);
    }
});