[
{"mnem:":"VEC SCALE=0, BRI=b, X=x, Y=y", "code":"0000_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx"},
{"mnem:":"VEC SCALE=1, BRI=b, X=x, Y=y", "code":"0001_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx"},
{"mnem:":"VEC SCALE=2, BRI=b, X=x, Y=y", "code":"0010_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx"},
{"mnem:":"VEC SCALE=3, BRI=b, X=x, Y=y", "code":"0011_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx"},
{"mnem:":"VEC SCALE=4, BRI=b, X=x, Y=y", "code":"0100_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx"},
{"mnem:":"VEC SCALE=5, BRI=b, X=x, Y=y", "code":"0101_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx"},
{"mnem:":"VEC SCALE=6, BRI=b, X=x, Y=y", "code":"0110_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx"},
{"mnem:":"VEC SCALE=7, BRI=b, X=x, Y=y", "code":"0111_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx"},
{"mnem:":"VEC SCALE=8, BRI=b, X=x, Y=y", "code":"1000_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx"},
{"mnem:":"VEC SCALE=9, BRI=b, X=x, Y=y", "code":"1001_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx"},

{"mnem":"CUR SCALE=s, X=t, Y=u",         "code":"1010_00yy_yyyy_yyyy ssss_00xx_xxxx_xxxx"},

{"mnem":"HALT",                          "code":"1011_0000_0000_0000"},

{"mnem":"JSR a",                         "code":"1100_aaaa_aaaa_aaaa"},

{"mnem":"RTS",                           "code":"1101_0000_0000_0000"},

{"mnem":"JMP a",                         "code":"1110_aaaa_aaaa_aaaa"},

{"mnem":"SVEC SCALE=c, BRI=b, X=d, Y=e", "code":"1111_geee_bbbb_hxxx", "details":"h is upper bit of c, g is lower bit"}
]