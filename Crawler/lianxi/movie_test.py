#coding=utf-8
'''
Created on 2018年7月15日

@author: kai.yangf
'''
import requests,re,time


response = requests.get('https://www.xphonecdn.com/move/7/2018-07-15/7dc2eed733802c607029bf65192b35ab.gif')
print (response.text)
filename = str(time.time()) + '.gif'
Path = 'E:\\Crawler\\CrawlerVidoe\\' + filename
with open(Path,'wb') as f:
    f.write(response.content)
    f.close()
    
    
http://438.m3u8xcdn.com/newmp4/20180709/90-mp4/index
<embed id="PlayerVideo_video_embed" 
src="/HLSPlayer/HLSPlayer.swf?v=1.5" 
type="application/x-shockwave-flash" 
allowscriptaccess="always" 
allowfullscreen="true" 
width="100%" 
height="600" 
flashvars="netstreambasepath=http%3A%2F%2Flocalhost%3A81%2FHLSprovider%2Fjwplayer5%2Findex58011.html
&amp;
id=player&amp;hls_debug=false&amp;
hls_debug2=false&amp;hls_lowbufferlength=3&amp;
hls_minbufferlength=-1&amp;
hls_maxbufferlength=60&amp;
hls_startfromlowestlevel=true&amp;hls_seekfromlowestlevel=true&amp;
hls_live_flushurlcache=false&amp;
hls_live_seekdurationthreshold=60&amp;
hls_seekmode=ACCURATE&amp;
provider=/HLSPlayer/HLS.swf&amp;
file=http://438.m3u8xcdn.com/newmp4/20180709/90-mp4/index.m3u8&amp;qualitymonitor.pluginmode=FLASH&amp;controlbar.position=over&amp;
image=https://www.xphonecdn.com/move/7/2018-07-15/bcebd4a4f456aaf6b6d074104c583221.gif">