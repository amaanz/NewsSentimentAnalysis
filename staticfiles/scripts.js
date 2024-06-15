let currentIndex = 0;
let articles = [];

function loadArticles(topic) {
    const topicSelect = document.getElementById('topic');
    const selectedTopic = topicSelect.value;

    fetch(`/get_articles?topic=${selectedTopic}`)
        .then(response => response.json())
        .then(data => {
            articles = data;
            currentIndex = 0;
            displayArticle(currentIndex, 'none');
        })
        .catch(error => console.error('Error loading articles:', error));
}


function handleTopicInputChange(event) {
    const topic = event.target.value;
    loadArticles(topic);
}

document.getElementById('topic').addEventListener('input', function(event) {
    loadArticles(event.target.value);
});


document.addEventListener('DOMContentLoaded', () => {
    const topicInput = document.getElementById('topic');
    topicInput.addEventListener('input', handleTopicInputChange);
});

function displayArticle(index, animation) {
    const newsCards = document.getElementById('news-cards');
    newsCards.innerHTML = '';

    const article = articles[index];

    const newsCard = document.createElement('div');
    newsCard.classList.add('news-card');
    if (animation === 'left') {
        newsCard.classList.add('slide-in-left');
    } else if (animation === 'right') {
        newsCard.classList.add('slide-in-right');
    }

    const imageContainer = document.createElement('div');
    imageContainer.classList.add('image-container');

    const img1 = document.createElement('img');
    img1.src = article.image_url;
    imageContainer.appendChild(img1);

    newsCard.appendChild(imageContainer);

    const titleContainer = document.createElement('div');
    titleContainer.classList.add('title-container');

    const titleLink = document.createElement('a');
    titleLink.href = article.article_url;
    titleLink.target = '_blank';
    titleLink.textContent = article.title;
    titleLink.classList.add('news-title');
    titleContainer.appendChild(titleLink);

    const sentimentGrade = document.createElement('span');
    sentimentGrade.textContent = `Sentiment Grade: ${article.sentiment}/10`;
    sentimentGrade.classList.add('sentiment-grade');
    titleContainer.appendChild(sentimentGrade);

    newsCard.appendChild(titleContainer);

    const sentiImage = document.createElement('img');
    sentiImage.src = article.senti_image;
    sentiImage.classList.add('senti-image');
    titleContainer.appendChild(sentiImage);

    const content = document.createElement('p');
    content.textContent = article.content;
    newsCard.appendChild(content);

    newsCards.appendChild(newsCard);
}

function prevArticle() {
    if (currentIndex > 0) {
        currentIndex--;
        displayArticle(currentIndex, 'left');
    }
}

function nextArticle() {
    if (currentIndex < articles.length - 1) {
        currentIndex++;
        displayArticle(currentIndex, 'right');
    }
}

window.onload = () => {
    const topicSelect = document.getElementById('topic');
    if (topicSelect) {
        topicSelect.addEventListener('change', () => loadArticles());
    }
    loadArticles(topicSelect ? topicSelect.value : 'default');
};

function togglePasswordVisibility(element) {
    const input = element.previousElementSibling;
    if (input.type === "password") {
        input.type = "text";
        element.classList.add("hide-password");
    } else {
        input.type = "password";
        element.classList.remove("hide-password");
    }
}

function loginUser() {
    document.getElementById('nav').innerHTML = '<a href="#" class="profile"><i class="fa fa-user"></i></a>';
}

function signUpUser() {
    document.getElementById('nav').innerHTML = '<a href="#" class="profile"><i class="fa fa-user"></i></a>';
}
