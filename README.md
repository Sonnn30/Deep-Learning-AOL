Project Deep Learning, membuat model deep learning untuk klasifikasi jenis material sampah, dimana terdapat 10 kelas, yaitu:
1. Metal
2. Glass
3. Organic Waste
4. Paper
5. Trash
6. Textile
7. Cardboard
8. Shoes
9. Plastic
10. E-Waste

Untuk mengembangkan modelnya kami menerapkan tranfer learning, dimana kami menggunakan pre trained model Restnet50, yang dimana model ini menerapkan konsep residual blok, yang dapat mengatasi masalah vanishing gradient
Untuk hasil dari model kami mendapatkan 95% akurasi.

Untuk appnya kami menggunakan gradio untuk mengembangkan tampilan UI, untuk menggunakannya kita hanya perlu mengupload gambar dan akan menghasilakn output dimana hasil outputnya menampilkan sebeapa confident model dalam memprediksi, dan selain label yang dikeluarkan,  informasi tambahan seperti cara mengolah sampah, dan apakah sampah tersebut dapat di recycle atau tidak, serta pengaruhnya pada lingkungan jika sampah tersebut tidak di olah dengan baik
