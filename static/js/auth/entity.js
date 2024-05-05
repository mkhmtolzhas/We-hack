document.querySelector('form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    const jsonData = JSON.stringify(Object.fromEntries(formData));
    console.log(formData);
    console.log(jsonData)

    try {
        const response = await fetch('http://127.0.0.1:8000/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: jsonData
        });
        if (response.ok) {
            // Перенаправляем пользователя на другую страницу
            const data = await response.json();
            console.log(data)
            window.location.href = '/login';
        } else {
            // Если ответ не успешный, обрабатываем ошибку
            console.error('Ошибка при регистрации:', response.status);
        }

        // Обработка ответа
    } catch (error) {
        console.error('Ошибка:', error);
    }
});