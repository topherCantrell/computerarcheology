################ Source files ##########################################

adventure/name	:= adventure
adventure/exe	:= $Oadventure/${adventure/name}
adventure/srcs	:= $(wildcard adventure/*.c)
adventure/objs	:= $(addprefix $O,$(adventure/srcs:.c=.o))
adventure/mans	:= $(wildcard adventure/*.6)
adventure/manz	:= $(addprefix $O,$(adventure/mans:.6=.6.gz))
adventure/deps	:= $(adventure/objs:.o=.d)

################ Compilation ###########################################

.PHONY:	adventure/all adventure/clean adventure/run

all:		adventure/all
adventure/all:	${adventure/exe}

adventure/run:	${adventure/exe}
	@${adventure/exe}

${adventure/exe}:	${adventure/objs} ${comlib}
	@echo "Linking $@ ..."
	@${CC} ${ldflags} -o $@ $^

################ Installation ##########################################

.PHONY: adventure/install adventure/uninstall adventure/uninstall-man

ifdef exed
adventure/exei	:= ${exed}/${adventure/name}

${adventure/exei}:	${adventure/exe} | ${exed}
	@echo "Installing $@ ..."
	@${INSTALL_PROGRAM} $< $@

install:		adventure/install
adventure/install:	${adventure/exei}
uninstall:		adventure/uninstall
adventure/uninstall:
	@if [ -f ${adventure/exei} ]; then\
	    echo "Removing ${adventure/exei} ...";\
	    rm -f ${adventure/exei};\
	fi
endif

ifdef mand
adventure/mani	:= $(addprefix ${mand}/,$(notdir ${adventure/manz}))

${adventure/mani}: ${mand}/%:	$Oadventure/% | ${mand}
	@echo "Installing $@ ..."
	@${INSTALL_DATA} $< $@

adventure/install:	${adventure/mani}
adventure/uninstall:	adventure/uninstall-man
adventure/uninstall-man:
	@if [ -f ${adventure/mani} ]; then\
	    echo "Removing ${adventure/mani} ...";\
	    rm -f ${adventure/mani};\
	fi
endif

ifdef scored
adventure/scorei:= ${scored}/adventure.scores
${adventure/scorei}:	| ${scored}
	@echo "Creating initial score file $@ ..."
	@${INSTALL_SCORE} $@

adventure/install:	${adventure/scorei}
endif

################ Maintenance ###########################################

clean:	adventure/clean
adventure/clean:
	@if [ -d $O/adventure ]; then\
	    rm -f ${adventure/exe} ${adventure/objs} ${adventure/deps} ${adventure/manz} $Oadventure/.d;\
	    rmdir $O/adventure;\
	fi

${adventure/objs}: Makefile ${confs} adventure/Module.mk $Oadventure/.d

-include ${adventure/deps}
