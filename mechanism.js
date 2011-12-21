// play button
javascript:
playmedia1(
    'playicon',
    // strID
    'player',
    // strURL
    '3ef1318b39b12607a2585483991338bfafa223adacb1202fefe4956c354fd6dade3abaa2704da30d2f1ced3fe51ffc51',
    // intWidth
    '355',
    // intHeight
    '68',
    // type
    'b3a7a4e64bcd8aabe4cabe0e55b57af5',
    // Head
    'http://m4.',
    // st_songid
    '2522250');
ListenLog(2522250, 0);

// core function
function playmedia1(
    playIcon,
    strID,
    strURL,
    intWidth,
    intHeight,
    type,
    Head,
    st_songid) {

    // {{{ display changes
	playIcon.replace(" ","%20");
	strID.replace(" ","%20");
	
	var objDiv=document.getElementById(strID);
	document.getElementById(playIcon).style.display='none';
	
	if (!objDiv) return false;
	if (objDiv.style.display!='none') {
		objDiv.innerHTML='';
		objDiv.style.display='none';
    // }}} display changes
	} else {
		if(strURL.indexOf('rayfile')>0) {
			var SongUrl = Head + strURL + GetSongType(type);
			objDiv.innerHTML=makemedia_html(SongUrl,intWidth,intHeight);
			objDiv.style.display='block';
		} else {
			$.ajax({
				type:'POST',
				url:'/time.php',
				cache:false,
				data:'str='+strURL+'&sid='+st_songid,
				dataType:'html',
				success:function(data){
					//alert(data);
					objDiv.innerHTML=makemedia_html(data,intWidth,intHeight);
					objDiv.style.display='block';
				
				},
				error:function(data){
					//alert('error');
				}
				});
		}
		
	}
}

function GetSongType(md5code)
{
	switch(md5code)
	{
		case "7d99bb4c7bd4602c342e2bb826ee8777":
			return ".wma";
			break;
		case "25e4f07f5123910814d9b8f3958385ba":
			return ".Wma";
			break;
		case "51bbd020689d1ce1c845a484995c0cce":
			return ".WMA";
			break;
		case "b3a7a4e64bcd8aabe4cabe0e55b57af5":
			return ".mp3";
			break;
		case "d82029f73bcaf052be8930f6f4247184":
			return ".MP3";
			break;
		case "5fd91d90d9618feca4740ac1f2e7948f":
			return ".Mp3";
			break;
	}	
}
