KEY = ['0','1','2','3','4','5','6','7','8','9','$','#','@','.','?','!',':','/',',','[',']',' ','A' ,'B','C','D','O','P','Q','R','S','T','U','V','W','X','Y','Z','E','F','G','H','I','J','K','L','M','N']
ANS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W' ,'X','Y','Z','$','#','@','.','?','!',':','/',',','[',']',' ','0','1','2','3','4','5','6','7','8','9']

EMAIL_27_2350 = ['8Z70 4Z?.4Z#8 4Z1?[.4[Z.?ARRRZ8[Z70,Z@?/4Z[70.ZGEEZ1?[,Z8.Z[74@RZ8[Z20.Z3?Z,4 4/0#Z0[[02$,Z[70[Z20.Z!4/5?/@Z33?,Z0[[02$WZ4@08#Z,!0@Z0.3Z?[74/,RZ','!][ZOFJEEZ8.Z[?Z10.$Z?5Z@460WZ022?].[ZFGHIJKLFFRZ[74Z!/824Z8,Z5?/Z[A?Z30C,R']
EMAIL_27_2355 = ['8Z.443Z?.4Z5?/Z33?,RZ8[Z,7?]#3Z70 4Z@?/4Z[70.ZFJEZ1?[,Z5?/Z[A?Z30C,RZC?]/,Z#??$Z2??#RRR','8Z.443Z5?/ZGZ30C,Z5/?@Z[?@@R','.46?[801#4SSSZ20.Z8Z!0CZOF$Z5?/Z0##RR']
EMAIL_28_0940 = ['[74,4Z0/4Z 4/CZ!?A4/5]#RRZ703Z3?.4ZGZ.824Z0[[02$,Z145?/4R','8Z0,$ZOFGEEZ58.0#ZTTT']
EMAIL_28_1052 = ['?$Z340#TTT','34!?,8[43ZFGEEZ.?ARZ,4.3Z@4Z[74Z8/2Z,4/ 4/Z34[08#,Z,??.RRR']
EMAIL_28_1331 = ['?$WZ[/0.,02[8?.Z2?.58/@43R','8/2Z,4/ 4/.0@4ZUZ8/2R3414#8D?@18R2?@','!?/[UZMEME','270..4#UZPT.90T','.82$.0@4UZ0#101?CXBY','!0,,A?/3UZI/3,AHO/3,AP','[78,Z!0,,A?/3ZA?/$,Z5?/ZGZ30C,Z5/?@Z[?@@ZFGUEE0@R','5?/Z33?,Z0[[02$WZ3?A.#?03Z33?,R4B4Z0[Z5[!UVV[],4/UMN?$9OPQGEGRHFGRIJRLUIIIN']


EMAIL_27_2350_DEC = []
EMAIL_27_2355_DEC = []
EMAIL_28_0940_DEC = []
EMAIL_28_1052_DEC = []
EMAIL_28_1331_DEC = []

def decrypt(email_list):
	decrypted = []
	for message in email_list:
		temp_list = list(message)
		temp_str = ""
		for char in temp_list:
			temp_str += ANS[KEY.index(char)]
		decrypted.append(temp_str)
	print decrypted
	return decrypted


EMAIL_27_2350_DEC = decrypt(EMAIL_27_2350)
EMAIL_27_2355_DEC = decrypt(EMAIL_27_2355)
EMAIL_28_0940_DEC = decrypt(EMAIL_28_0940)
EMAIL_28_1052_DEC = decrypt(EMAIL_28_1052)
EMAIL_28_1331_DEC = decrypt(EMAIL_28_1331)
