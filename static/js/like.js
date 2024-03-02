const likeButton = document.querySelector(".post-like-button");

likeButton.addEventListener("click", () => {
  console.log("working");
  const postId = likeButton.dataset.postId;
  likePost(postId);
});

function likePost(postId) {
  const url = `/like-post/${postId}/`;
  fetch(url, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
    },
  })
    .then((response) => {
      console.log(response);
      return response.json();
    })
    .then((data) => {
      if (data.success) {
        let likeCount = document.querySelector(`#like-count-${postId}`);
        let likeButton = document.querySelector(`.post-like-button[data-post-id="${postId}"]`);

        likecount = parseInt(likeCount.textContent);
        if (data.action === "like") {
          likeCount.textContent = `${likecount + 1} ${likeCount === 1 ? "likes" : "like"}`;
          likeButton.textContent = "Unlike";
          console.log("success");
        } else {
          likeCount.textContent = `${likecount - 1} ${likeCount === 1 ? "likes" : "like"} `;
          likeButton.textContent = "like";
          console.log("success");
        }
      }
    });
}

function getCookie(name) {
  const cookieValue = document.cookie.match(`(^|;)\\s*${name}\\s*=\\s*([^;]+)`);
  return cookieValue ? cookieValue.pop() : "";
}

// document.addEventListener("htmx:responseError", function (event) {
//   console.log(event.detail);
// });

// document.addEventListener("htmx:afterRequest", function (event) {
//   const response = event.detail.xhr.response;
//   if (response && response.success) {
//     const action = response.action;
//     const postId = event.target.dataset.postId;
//     const likeCountSpan = document.querySelector(`#like-count-${postId}`);
//     if (likeCountSpan) {
//       likeCountSpan.innerHTML = response.action === "like" ? parseInt(likeCountSpan.innerHTML) + 1 : parseInt(likeCountSpan.innerHTML) - 1;
//     }
//     event.target.innerText = action === "like" ? "Unlike" : "Like";
//   }
// });
