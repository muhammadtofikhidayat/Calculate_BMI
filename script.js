function calculateBMI() {

  var weight = document.getElementById("weight").value;
  var height = document.getElementById("height").value;

  if (weight === "" || height === "") {
    alert("Mohon masukkan berat dan tinggi badan terlebih dahulu.");
    return;
  }

  var bmi = (weight / ((height / 100) * (height / 100))).toFixed(2);
  var result = "";
  var keterangan = "";

  if (bmi < 18.5) {
    result = "Kekurangan Berat Badan";
    keterangan = "<p>Makanan penambah berat badan yang umum bisa Anda temukan pada daging dan ikan. Konsumsi produk susu juga penting untuk menambah berat badan anak. Berikut jenis makanan penambah berat badan secara umum yang bisa Anda coba:</p> <p>1.Sayuran berwarna hijau gelap, seperti bayam, kale, dan arugula</p><p>2.Protein hewan, seperti daging sapi, paha ayam, dada ayam, kalkun, ikan salmon, udang, dan jenis ikan lain</p> <p>3.Buah dan sayuran, seperti kembang kol, wortel, mentimun, tomat, pisang, apel, alpukat, dan beri</p> <p>4.Kacang-kacangan, seperti kedelai, tahu, buncis, kacang hitam, lentil, kacang almond, kacang mete, biji rami, selai kacang, dan mentega Makanan kaya karbohidrat, seperti nasi putih dan nasi merah</p><p>5.Minuman dan makanan dari susu, seperti keju, yogurt, dan susu</p><p>6.Minyak dan lemak sehat, seperti mentega, margarin, dan minyak zaitun</p><p>7.Telur ayam</p><p>8.Kelola stress dan perbanyak olahraga.</p>";
  } else if (bmi >= 18.5 && bmi < 24.9) {
    result = "Berat Badan Ideal";
    keterangan = "<p> Selamat Berat Anda Ideal ! </p> <p> 1. Kurangi cemilan tinggi GGL dan mengkonsumsi lebih banyak buah dan sayur Camilan tinggi gula, garam, dan lemak tidak hanya bisa memicu penyakit jantung, diabetes, dan penyakit lainnya tapi juga bisa menambah berat badan Anda. Agar tetap menikmati makanan manis dan segar tanpa menambah berat badanmu, Anda bisa memakan pepaya, nenas, anggur, salad sayur atau buah dan sayur lainnya sebagai alternatif camilan. Selain bisa menikmati enaknya buah dan sayur, juga bisa mendapat kaya manfaat seperti vitamin dan antioksidan! </p><p> 2. Lakukan aktivitas fisik 30 menit per hari Anda tidak diharuskan untuk berolahraga intens selama 30 menit per hari, olahraga ringan seperti jogging, sit up, atau naik-turun tangga juga sudah cukup. Anda bisa mengurangi penggunaan kendaraan bermotor dan menggantinya dengan bersepeda atau berjalan kaki ketika bepergian di area sekitar rumah. </p> <p> 3. Istirahat yang cukup Ternyata begadang bisa mempengaruhi kenaikan berat badan karena meningkatkan hormon yang bisa meningkatkan nafsu makan dan mengganggu metabolisme tubuh. Oleh karena itu, sesuai anjuran CDC pastikan Anda tidur 8 – 10 jam setiap hari.</p>";
  } else if (bmi >= 25) {
    result = "Obesitas";
    keterangan = "<p>Berat Anda melebihi berat ideal Prinsip dasar penatalaksanaan obesitas yang dianjurkan badan dunia adalah diet rendah energi seimbang dengan pengurangan energi 500-1000 kkal dari kebutuhan sehari dengan cara : </p> <p>1.Mengurangi konsumsi bahan makanan sumber karbohidrat kompleks seperti nasi, roti, jagung, kentang dan sereal</p> </p> <p>2.Menghindari konsumsi bahan makanan sumber karbohidrat sederhana seperti gula pasir, gula merah, sirup, kue yang manis dan gurih, madu, selai, dodol, coklat, permen, minuman ringan, dll </p> </p> <p>3.Mengurangi konsumsi bahan makanan sumber lemak dengan tidak mengolah makanan dengan cara digoreng dan menggunakan santan kental serta mentega dan margarin</p> <p>4.Mengutamakan konsumsi bahan makanan sumber protein rendah lemak, seperti ikan, putih telur, ayam tanpa kulit, susu dan keju rendah lemak, tempe tahu, dan kacang-kacangan yang diolah</p>";
  } else {
    "ada kesalah memasukan berat dan tinggi badan"
  }

  document.getElementById(
    "result"
  ).innerHTML = `BMI anda ${bmi}. Kategori:  ${result}.`;


  document.getElementById(
    "result_informasi"
  ).innerHTML = `<h1> ${result}</h1>
  <h2>  BMI anda ${result}</h2>
  <div class="popup__text">
    ${keterangan}
  </div `;
}


