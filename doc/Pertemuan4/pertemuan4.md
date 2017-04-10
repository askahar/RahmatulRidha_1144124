RUANG KEADAAN
Pembahasan 
Ruang keadaan adalah sustu cara untuk mendefinisikan suatu permasalahan kedalam bentuk Representasi Algoritma. 
Ruang keadaan juga merupakan suatu ruang yang berisi semua keadan yang memungkinkan sehingga secara umum untuk 
dapat mendeskripsikan masalah dengan baik.
Contoh :
Pada Kasus Petani, Ayam, Gabah dan Harimau 
Seorang petani akan menyeberangkan seekor ayam, seekor harimau, dan gabah dengan sebuah boat yang melalui sungai. 
Boat hanya bisa memuat petani dan satu penumpang yang lain (ayam, gabah atau harimau). Jika ditinggalkan oleh petani 
tersebut, maka gabah akan dimakan oleh ayam, dan ayam akan dimakan oleh harimau. 
Penyelesaian: 
1.	Identifikasi ruang keadaan. 
Permasalaahn ini dapat dilambangkan dengan (JumlahAyam, JumlahHarimau, JumlahGabah, JumlahPetani). 
Sebagai contoh Daerah asal (1,1,1,1) berarti daerah asal ada ayam, ada harimau, ada gabah, dan ada petani. 

2.	Keadaan awal dan tujuan 
o	Keadaan awal, pada kedua daerah: Daerah asal : (1,1,1,1), Daerah seberang: (0,0,0,0) 
o	Tujuan, pada kedua daerah: Daerah asal: (0,0,0,0), Daerah seberang: (1,1,1,1) 

3.	Aturan-aturan 
ATURAN KE -  |	ATURAN 
------------- | -------------------- 
1	Petani menyeberang
2	Petani kembali
3	Ayam menyebrang
4	Ayam kembali 
5	Gabah menyeberang 
6	Gabah kembali
7	Harimau menyeberang 
8	Harimau kembali 


 
Solusi : 
DAERAH ASAL | DAERAH SEBERANG | ATURAN YANG DIPAKAI
------------ | ------------ | ------------- 
(1,1,1,1)	(0,0,0,0)	1,3
(0,0,1,1)	(1,1,0,0)	2
(1,0,1,1)	(0,1,0,0)	1,7
(0,0,1,0)	(1,1,0,1)	2,4
(1,1,1,0)	(0,0,0,1)	1,5
(0,1,0,0)	(0,1,0,0)	2
(1,1,0,0)	(0,0,1,1)	1,3
(0,0,0,0)	(1,1,1,1)	Solusi


