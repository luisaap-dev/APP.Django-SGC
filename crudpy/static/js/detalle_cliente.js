const imgInput = document.getElementById('id_foto');
  const imgPreview = document.getElementById('img_preview');
  imgInput.addEventListener('change', () => {
    const file = imgInput.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        imgPreview.src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  });

  
function confirmDelete() {
  const myModal = new bootstrap.Modal(document.getElementById('confirmModal'));
            myModal.show();
            return;
}


function saveChanges() {
  
  const myModal = new bootstrap.Modal(document.getElementById('confirmSaveModal'));
            myModal.submit();
            return;
}