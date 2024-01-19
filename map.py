tileMap = ["WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
           "W...W.............................................................................................PW",
           "W...W.WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW.W",
           "W...W...W.....WPWWWW...W.W...WWW...W.......W...W...W....PW....WPW....W.....W........W...W...WPWWPW.W",
           "WWPWW.W...WWW.W......W.....W..WP.W.W.WWW.W.W.W.WPP.W.WWWWWWWW...W.WW.W.WWW.WPWW.W.W.W.W.W.G.W....W.W",
           "W.1111WWWWW111W.WWWW.WWWWW.WWWWWWW...W.W.WP..W....PW..WWW.....WPW.W..W.....WWWW.W.W.WPW.W...WWWW.W.W",
           "W.WWW111W111W111W....W.....WP....WWWWW.W.WWWWWWWWWWWW.W...W.WWWWW.WWWW.WW.WW....W.W.W.W.WWW.W....W.W",
           "W.W.W.W1W1WWWWW1WW.WWW.W.W.......W.....W........W...W.W.WWWWWGW.........W....WW.W.WP..W...W.W.WWWW.W",
           "W...W.W111W11111WP.....W.WWW...G.W.P.WWWWWWWW.W.W.W........WW.W.W.WWWWW.W.WWWW..W.WWWWWWW...W....W.W",
           "WWWWW.WWWWW1WWWWW.WWWWWW...W.....W...W......W.W.W.WWWWW.WW.W..W.W.W...W.....W..WW.W...W...W.W.WW.W.W",
           "W.....W....1W.....W......W.WWWWWWWWWWWWWWPWWW.WWW.....W.P..W.WW.W...P.WWW.W.WWWW..WPW.W.WWW......W.W",
           "W.WP...PW.W1WWWWWWWW.P.W...W....................WWW.WWWWWW.W....WWW...W.....WP...WW.W.W.W...WWW.WW.W",
           "W.WWW.WWW.W11111111W..PWWWWW.WWWWWWWWWWWWWWWWW......W......W.WWWW.WWWWW.WWWWWWWW.WW.W.W.W.WWW....W.W",
           "W.W...W...W.WWWWWW1WWWWW.......W...WGWW.....W..WW.W.W.WWWWWW.W....WW......WW...W....W...W...WWWW.W.W",
           "W...W.WWW.W...W.PW1W...WPW.WWW...W...W..W.W....WWWP.W.P........W...WWWWWW.W..W...WWWWWWWWWW..W...W.W",
           "W.WWW.......W....W1WW.WWWW.WWWWWWWWWWWWWW.WWWWWWWWWWWWW.W.WWWWWWWW.W...W..W.WWWWWWW...W...WW.WWWWW.W",
           "W.PWWWWWWWWWW.WWWW1W....W...W111111111111111111111111111W.WWP...PW...W.W.WW...W...W.W.W.W......W.W.W",
           "WWWW.....W..W.W1111W.WW...P.W1WWWW.WWWWWWWWWWWWWWWWWWWW1W.....P..W.WWW.W.W..W...W...WGW.WWWWWW.W.W.W",
           "WPWW.WWW...WW..1W.WW....W.P.W1W.P......W.W.........111W1WWWWP...PW...W...W.WWWWWWWWWWWW.W........W.W",
           "W......WWWWWWWW1W.WWWWWWWWW.W1WWWWWWW.WW.W.WWW.WWWW1W111W..WWWWWWWWW.WWWWW...W..W..PWPW.W.WWWWWW.W.W",
           "W.WWWW..11111111W....W......W11W.........W...W.W..W11WWWWW.WW........W...WWW.WW...WWW.W.W......W.W.W",
           "W....WWW1W.W.WW.W.WWWW.WWWW.WW1W.PGP.WWW.WWW.....WWW11111W..W.WWWW.WWW.W........WWW...W.WWWW.P.W.W.W",
           "WWWW.WWW1W.W..WWW...WWWW.....W1W.....W....PWWWWWPW...WWW1WW...W......W.WWWWWWWW.W...W...W..W...W.W.W",
           "W....W111W.WWWWWWWW.P.W..WWWWW1WWWWWWW.WWWWW...WWWWWWWWW11W.W.W.WWWW.W.W...W....WWWWWWWWW.WWWWWW.W.W",
           "W.WW.W1WWWWWW11111W.W.W.WW11111...PW...W...W.WWW111111WWW1..W.....W..WPW.W.W.P.WWWWW..W.....WW.W.W.W",
           "W..W.W11111111W.W1W...WWW11WWWWWWWWWWW...W...W111WWWW11111W.WWWWW.W.WWWW.W.W.P.WP...W.W.WWW.W..WPW.W",
           "W..W.WWWWWWWWWW.W1WWWWWW11WW.....WW.GW.WWWWWWW1WWWWWWWWWWWW.P.W...W.WW...W.WP.PWWWW.W.W.W...W..WWW.W",
           "W.......PW......W11111111WW..WWW....WW....W...111111111111WWW.WWW.W..W.WPW.WWW.W....W.W.W.WWW....W.W",
           "W..WWWWWWW.WWWWWWWWWWWW.WW..WWWWWWWWWWWWW.W.WWWWWWWW.WWWW1W.....W.W.WW.WWWPW...W.WWWW...W...WWWW.W.W",
           "W.............WPW11111W.W..WW.P.W1111111W.........WW.WWWW1W.WWW.W....W...WWW.WWW....WWW.WWW...W..W.W",
           "W.WWWW.W.WWWW.W.W1WWW1W.P.WWWP.PW1WWWWW1WWWWWWWWW..WPW1111W...W.WWWW.W.W.......WWWW.W.W.W...W.W.WW.W",
           "W..W...W....WWW.W11WW1WWWWWWW.P.W1W....1W.W11111WWPWWW1WWWWWW.W...PW.W.WW.WWWWWW....W.W.W.WWW.W..W.W",
           "WW.W.W.W.WWWW111WW1WW1WWW111WW.WW1W.WWW1WWW1W.W11WWWW11WP.....WWWWWW....W..1111W.W.WW.W.W..P..WW.W.W",
           "W..W.W...W1111W1111WW11111W1111111W...W11111WPWW11WWW1WWWWWWWWW...WWWWWWW.W1WW111W.W..W.W.WWW.W..W.W",
           "W.WW.WWWWW1WWWWWWWWWWWWWW111WWWWWWWWW.WW.WWWW.WWW11111W....P..W.W.W...W...W11WWW1W.W.WW.W.....W.WW.W",
           "W..WP...PW1W1111W...W...WWWWW...WWW...WW...P..WPWW.WWWW.W.W.W.W.W...W.W.W.WW111W1W...W..WWWW.WW..W.W",
           "WW.W..P..W111WW1W.G...W.......W...W.WWWW.WWWWWW.WW.W....W.P..PW.WWW.W...W.WWWW1W1WWWWW.WWP...WWWWW.W",
           "W..W..P..WWWWW11W...WWWWWWWWW.W.W....WPWWWP...W..W...WWWWWWWWWWWWWWWWWWWW....W1W11111W..WWWWWWPP.W.W",
           "W.WWP...PW...W1WWWWWW.PW...WWPWWWWWW.W...WWW.WWW.WWWWW111111111111111111W.PP.W1WW.WW1WW.WP.WWW.W.W.W",
           "W.GWWWWWWW...W1111WWP.WW.W..WWW......WWW...W...W.....W1WWWWWWWWWWWWWWWW1W.PP.W11W..W1W..WW.....W.W.W",
           "WWWW11111W.WWWWWW11WW....WW.....W.WWWW...W.W.W.W.WWW.W1111W........WWWW1W....WW1WW.W1WW..W.WWW...W.W",
           "W1111WWW1W.W1111WW11WWWWWWWWWWWWW.WW...W.W...W.W.....W.WW1W.P....P.W1111WWWWWWW1W..W11WWPWWWW..WWW.W",
           "W1WWWW.W1WWW1WW11WW1WW1111111WP....W.WWWWW.WWW.WW.WWWWPWW1W...GG...W1WWWWW111111W.WWW11WWWW...WW.W.W",
           "W1W....W11111WWW1111WW1WW.WW1WWWWW.W11111W..PW.W111WGWWW11W.P....P.W11WWWW1WWW.WW...WW11W.WWW....W.W",
           "W1WWWWWWWWWWWWWWWWWWWW1WP.PW11111WWW1WWW1W.WWW.W1W1WWWW11WW........WW1WWWW11W..W..W.PWW1W...W.WW.W.W",
           "W1W1111W.WWWWWW.....PW1WWWWW1WWW11111W111W.....W1W1WW111WWWWW.W.WW...1WWWWW1W.WW.WWWWWW1WWW.W.W..W.W",
           "W111WW1W.W1111W.WWWWWW1111111WWWWWWWWW1WWWWWWWWW1W1111WWWWWWW.W.WWWWW1WW1111W..W.W111111W.....W.WW.W",
           "WWWWWW1WWW1WW11111111WWWWWWW1WG.....W11WWWWW111W1W.WWWW.......W..W1111W11WWWWW.W.W1WWWWWW.WWWWW..W.W",
           "W....W111W1WWWWWWWWW11WWWWWW1W......W1WWWW111W111W....W.W.WWW.WW.W1WWWW1WW111W...W1111..W...W.WW.W.W",
           "WGWW.WWW111W.WPPWGWWW1WWW1111W......W111111WWWWWWWWWW...W..W...W.W111111WW1W1WWWWWWWW1W...W.W....W.W",
           "WWWW...WW.WW.WPPW.W..11111WWWW..PPP.WWWWWW..PW111111W.WWWW...W.W.WWWWWWWWW1W1111111111WWWWW.W.WWWW.W",
           "W....WWWW.W..W.WW...WWWWWWWWWWWWW.WWWP...W.WWW1W.WW1W.WP.WWWWW.W......WWWW1WWWWWWWWWWWW.....W....W.W",
           "W.WWWW....W.WW..WWWWWW1111111WWWW111WWWW...W111W.W11W.WW.....W...WWWW.W1111W............WWWWW.WW.W.W",
           "W......WWWW.WWW..W.1111WWWWW1WW111W1111WWWWW1WWW.W1WW..WWW.W.WWW......W1WWWW.WWW.WWWWWWWWWW...WW.W.W",
           "WWWWWW.W111111WW..W1WWWW...W1111WWW1WW1111WW1W...W1WWW.....W.WPW.WWWWWW1W....W...W......W...W....W.W",
           "W1111WWW1WWWW11WWWW1W....W.WWWW111W1111WW1111W.W.W111WWWWW...W.W..W11111W.WWWWPWWW.WWWW...WWW.WW.W.W",
           "W1WW11111WP.WW111WW1W.WWWW...PWWW111WWWWWWWWWW.W.WWW1W111WWWWW...WW1WWWWW.WW....W....PW.WWWPW....W.W",
           "W11WWWWWWWW.WWWW1111W..W.WWWWWWWWWWWWP.........W...W1W1W1W111WWWWWW1WPWW...WWWW.W.WWW.W.....WWWWWW.W",
           "WW1WWG..W.....WWWWWWWW...WP.PW.G.WP...WWWWWWWWWWWW.W1W1W1W1W1W111WW1W....W......W.W.....WWW....WGW.W",
           "WW11WWW.W.WWW...WW...W.W.W.W.W...WWWWWWW.W.........W1W1W1W1W1W1W1111WWWWWWWWWWWWW.W.WWW...WWWW.W.W.W",
           "WWW111W.W.....W....W...W....PWW.WWW.W....W.W.W.WWWWW1W1W1W1W111WWW.WWGGGGGGGGGGGW.W.W.WWW...W..W.W.W",
           "W.WWW1W.WWWWWWWWWWWWWW.WWWWWWW......W.W.WW.W.......W1W1W111WW.WWPW..WGWWWWWWWWWGW.W.W...WWW.W.WW.W.W",
           "W..WW1W.......WW.......W11111WWW.WW.WWW....W.WWWWW.W111WWWWW..W..WW.WGW.......WGW.W...W.W...W.PW.W.W",
           "WWWW11WWWWWWW....WWWW.WW1WWW111W....WP..WWWW...WWW.WWWWW.....WW.WW..WGW..P....WGW.WWWWW.W.WWWW.W.W.W",
           "WW111W111111WWWWWW....W11WGWWW1WWW.WWWWWW....W..WW.WPP.W.WWWWW..W..WWWW..P....WGW.PW....W...W..W.W.W",
           "W11WW11WWWW1WW111..WWWW1WW...W1111111111WWWWWWW....WP......W...WW.WW.....P....WGW.WWW.W.WW.WW.WW.W.W",
           "W1WWW1WW.PW1111W1WWW..W11WWW.WWWWW.WWWW1111W..WPWWWW..WWWW.W.W.W.....WW..P....WGW.....W.....W..W.W.W",
           "W1WWW1W..WWWW.WW11W..WWW1W.....PWW.WWWWWWW1WW.WWW.W..WW......W...WW.WWW..PPP..WGWWWWWWWWWWWWWW.W.W.W",
           "W1WW11W.WWWW..PWW1W.WW111W.WWWWWW111111WGW1W....W....WW.WWWW.WWWWW..WGW.......WGW...........W..W.W.W",
           "W1111WW......WWWW1W..W1WWW......W1WW.W1WWW1W.WW.WWWW.WW..WW..W.W...WWGWWWWWWWWWGW..G..P..G..WPWW.W.W",
           "WW.WWWWWWWWW.W1111WW.W111WWWWWW.W11W.W1WW11W.PW.......WW....WW...W..WGGGGGGGGGGGW...........W....W.W",
           "W....PWW111W.W1WWWW..WWW1WW111W.WW1WPW1111WWWWWWWW.WWWWWWWWWWWWWWWW.WWWWWWWWWWWWWWWWWW.WWWWWWWWWWW.W",
           "WWWWWWW11W1WWW1111..WW111WW1W1W.WW1WWWWWWWW...111111111111111111W.W.W...W...WWPP...WW...........PW.W",
           "W1111111WW11WWWWW1W..W1WWWW1W1WWW11W...W....WW1WWWWWWWWWWWWWWWW1WPP.W.W...W..WWPWW.W..WWWWWWWWW.WW.W",
           "W1WWWWWWWWW1111111WW.W111WW1W11111WW.W.W.WW..W1W1111WWWWWW...WW1WWWWW.WWWWWW..WWWW.WWWW....WW....W.W",
           "W11111111WWW.WWWWWW..WWW1WW1WWWWW....WPW.PWW.W1W1WW1111W...W.PW11111W......WW....W......WW..W.WWWW.W",
           "WWWWWW.W1WW...WW.WWWWW111WW1W..WWWWW.W.WWWWW.W111WWWWW1W.WWWWWWW.WW1WWWWWW.WWWWW.WWW..W..WW...W.PW.W",
           "W...W..W11W.W....W11111W.WW1WWWW111W...W111WWWWWWW11111W......WW.W11W....W.W...WWW...WWW..WWWWW.WW.W",
           "W.W...WWW1WWWW.WWW1WWWW...W111111W1WWWWW1W1111W.W11W.WWWWWWWW....W1WP.WW.W...W.....WWWPWW.W...W..W.W",
           "W.WWW.WPW11WWWWW111W..WWW.WWWWWWWW1W11111WWWW1WWW1WW.W...WWWWWWWWW1WWWW..WWWWWWW.WWW......W.W.WW.W.W",
           "W.W...W.WW1WW1111WWW........WWG..W111WWW.W..W11111W....W....WWW.......W.WW...W..PPPW.WWWWWW.W....W.W",
           "W.WWWWW..W1111WWWW.W.WWWWWW.WW..PWWWWW.W.WW.WW.WWWWWWWWWWWWWWPW.......W....W...WPPPW......WWWWWW.W.W",
           "W.....WW.WWWWWW.......WPW....W.P..........W..WWW...W..W.......W1WW.WW.W..WWWWW.WWWWWWWWW.........W.W",
           "WWW.W..W........WWWWWWW.W.WW.WWWWWWW.WWWW.WW.....W...WW.WWWWWWW1WW.W..W..W...W.........WWWWWWW.WWW.W",
           "W...WWWWWWWWWWWWWW...W....WW.....W....W....WWW.WWWWW......W11111W.PW.WW.WW.W.WWWWWW.WW.......W...W.W",
           "W.WWW...WW...W.WGW.W.WWWWWWWWW.W.W.WW.W.WW..PW..W..WWWWWWWW1W.WWWWWWP......W.........W.WWW.W.WWW.W.W",
           "W.....W....W.W.WGG.W...WW.W....W.W....W..WWWWWW.WW..W11111W1W...W.WWWWWWWWWWWWWWWWWW.W.W...W...W.W.W",
           "W.WWW.W.WWWW...WWWWWWW.W..W.WWWW.WWWW...WW.......WW.W1WWW111WWW.W.....PWWW111111111W...W.WWWWW...W.W",
           "W...W.W..W...W.......W.W.WW....W...WWWWWWW.WW.WW.W..W1111WWWW.....WWWWWW111WWWWWWW1WWW.W.....WWWWW.W",
           "WWW.W.WW.WWWWWWWWW..WW.W..WWWW.WWW.W...P...W...W.W.WWWWW1..WW.WWW.W111111WWW.WWWWW1W...W.WWW....WW.W",
           "W...W.......W....W.WW..WW....W.WP..W..P.P..W...W.W.W..W11W....WWWWW1WWWWWW...W111W1W.WWWWW...WW..W.W",
           "W.WWWWWWWWW.WWWW.W.W..WWWWWW...WWW.W.P...P.W...W.W.W.WW1WWWWWWW111W1W111W.WWWW1W111W.....W.WWWWWWW.W",
           "W......W.........W...WW...WWWWWW.W.WP..G..PWW.WW.....W11W1111111W1W111W1W.W1111WWW.WWWWW...WGGGGGW.W",
           "W.WW.WWW.WWWWW.WWWWWWW..W.WPWWW..W.WWWWWWWWWW..WWWWWWW1WW1WWW.WW11WWWWW1W.W1WWWWWW.W111W.WWWGGGGGW.W",
           "W..W.....WP..W.......WWWW.W.WW.....W....W...WW...W...W1111W....W1WWWWWW1W.W1W1111WPW1W1WWW11GGGGGW.W",
           "WW.WWWWWWW.WPWWW.W.W...W..W.WW.WWWWWWWW.W.W..WWW.W.W.WWWWWW.WWWW1W111111W.W111WW1WWW1W11111WGGGGGW.W",
           "W............WP..W...W...WW....WP.........WW.......W............111WWWWWW.WWWWWW11111WWWWWWWGGGGGWGW",
           "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
           ]