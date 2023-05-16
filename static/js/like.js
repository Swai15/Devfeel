const likeButton = document.querySelector(".like-button");

likeButton.addEventListener("click",() => {
  const postId = likeButton.dataset.postId;
  likePost(postId);
});

function likePost(postId) {
  const url = `/like-post/${postId}/`;
  fetch(url,{
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
        const likeCount = document.querySelector(`#like-count-${postId}`);
        const likeButton = document.querySelector(`.like-button[data-post-id="${postId}"]`);

        likecount = parseInt(likeCount.textContent);
        if (data.action === "like") {
          likeCount.textContent = `${likecount + 1} ${likecount === 1 ? "likes" : "like"}`;
          likeButton.textContent = "UnLike";
        } else {
          likeCount.textContent = `${likecount - 1} ${likecount === 1 ? "likes" : "like"} `;
          likeButton.textContent = "like";
        }
      }
    });
}

function getCookie(name) {
  const cookieValue = document.cookie.match(`(^|;)\\s*${name}\\s*=\\s*([^;]+)`);
  return cookieValue ? cookieValue.pop() : "";
}