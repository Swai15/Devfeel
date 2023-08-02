// const commentForm = document.querySelector('#comment-form');
// const commentSection = document.querySelector('.comment-section');
// const postId = commentForm.dataset.commentId;


// commentForm.addEventListener('submit',(e) => {
//   e.preventDefault();


//   const commentInput = document.querySelector('[name="comment-text"]');
//   const commentText = commentInput.value.trim();

//   fetch(`/submit-comment/${postId}/`,{
//     method: "POST",
//     credentials: "same-origin",
//     headers: {
//       "Content-Type": "application/json",
//       "X-CSRFToken": getCookie("csrftoken"),
//     },
//     body: JSON.stringify({ 'comment-text': commentText })
//   })
//     .then((response) => {
//       console.log(response);
//       response.json();
//     })
//     .then((data) => {
//       if (data && data.success) {
//         const newComment = document.createElement('div');
//         newComment.classList.add('comment');
//         newComment.innerHTML = `
//         <p>${data.comment.text}</p>
//         <p>By: ${data.comment.author} </p>
//       `;

//         commentSection.appendChild(newComment);
//         commentInput.value = "";
//       }
//     })
//     .catch((error) => {
//       console.log("Error",error);
//     });


// });

// function getCookie(name) {
//   const cookieValue = document.cookie.match(`(^|;)\\s*${name}\\s*=\\s*([^;]+)`);
//   return cookieValue ? cookieValue.pop() : "";
// }


const firstComment = document.querySelector('.no-comment');
const commentInput = document.getElementById('comment-input');

firstComment.addEventListener('click',() => {
  commentInput.focus();
});