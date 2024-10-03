

NaturaLingua can create bilingual documents (.pdf and .txt), to help you to learn new languages.

Example of resulting .pdf and .txt files are in the folder directoryYoutube.

To create your own bilingual files with the movie or the youtube video you want, the code to use is in main.py. You can get ideas of youtube channels or of movies in the files youtube.txt and movies.txt.

As the input, you can either :

A) use two subtitles files from a movie : one subtitle file for the language you learn, one subtitle file for the language you already know.
    You can find subtitle files , either
		1) On www.opensubtitles.org or another website with subtitle files (choose files using the .SRT format) ;
    2) Or from Netflix if you use Devtools Network, to find the two .VTT files.
If you download subtitle files (not using netflix), you need to install "ffsubsync" on your computer. My python code use this program to sync the two files.

B) Or you can use the ID of a youtube video that has subtitles in the two languages you are interested in (one you know, one you learn). The ID of a youtube video is in its URL. It is a string of 11 characters. This B) option need two steps to be enabled :
	1) to create a Youtube API key : https://console.cloud.google.com/apis/credentials?pli=1
	2) And then To create a .env file in the "youtube folder" containing the line :
YOUTUBE_KEY=......
(replace ...... with your Youtube API key)

If you struggle with those preliminary steps of the B) technique, you can still create bilingual documents from a youtube video : use online tools to create .SRT files from the youtube video, then use the A) technique with those .SRT files.

