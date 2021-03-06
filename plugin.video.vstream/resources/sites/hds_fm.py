# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# source 35 https://www1.hds.fm/films-streaming/ 29112020
# update 07012020
import re

from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import progress


SITE_IDENTIFIER = 'hds_fm'
SITE_NAME = 'Hds-fm'
SITE_DESC = ' films et series'

URL_MAIN = 'https://www1.hds.fm/'

MOVIE_NEWS = (URL_MAIN + 'films-streaming/', 'showMovies')
MOVIE_GENRES = (True, 'showMovieGenres')
MOVIE_VOSTFR = (URL_MAIN + 'film/VOSTFR/', 'showMovies')
MOVIE_VF_FRENCH = (URL_MAIN + 'film/French/', 'showMovies')

MOVIE_HDLIGHT = (URL_MAIN + 'qualit/HDLight/', 'showMovies')

SERIE_NEWS = (URL_MAIN + 'serie-tv-streaming/', 'showMovies')
SERIE_GENRES = (True, 'showSerieGenres')

SERIE_VF = (URL_MAIN + 'serie/VF/', 'showMovies')
SERIE_VOSTFR = (URL_MAIN + 'serie/VOSTFR/', 'showMovies')

key_search_movies = '#searchsomemovies'
key_search_series = '#searchsomeseries'
URL_SEARCH = (URL_MAIN + 'search/', 'showMovies')
URL_SEARCH_MOVIES = (key_search_movies, 'showMovies')
URL_SEARCH_SERIES = (key_search_series, 'showMovies')

# recherche utilisée quand on n'utilise pas le globale
MY_SEARCH_MOVIES = (True, 'MyshowSearchMovie')
MY_SEARCH_SERIES = (True, 'MyshowSearchSerie')

# Menu GLOBALE HOME
MOVIE_MOVIE = (True, 'showMoviesSource')
SERIE_SERIES = (True, 'showTvshowSource')


def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_SEARCH[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche Films & Séries', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_MOVIES[1], 'Recherche Films', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films (Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_VF_FRENCH[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_VF_FRENCH[1], 'Films (French)', 'vf.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_VOSTFR[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_VOSTFR[1], 'Films (VOST)', 'vostfr.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HDLIGHT[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_HDLIGHT[1], 'Films (HD Light)', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_SERIES[1], 'Recherche Séries ', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Séries (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_GENRES[1], 'Séries (Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_VF[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VF[1], 'Séries (VF)', 'vf.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_VOSTFR[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VOSTFR[1], 'Séries (VOST)', 'vostfr.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMoviesSource():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_MOVIES[1], 'Recherche Films', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films (Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_VOSTFR[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_VOSTFR[1], 'Films (VOST)', 'vostfr.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', [0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_VF_FRENCH[1], 'Films (French)', 'vf.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showTvshowSource():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MY_SEARCH_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, MY_SEARCH_SERIES[1], 'Recherche Séries ', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Séries (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_GENRES[1], 'Séries (Genres)', 'series.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_VF[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VF[1], 'Séries (VF)', 'vf.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_VOSTFR[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VOSTFR[1], 'Séries (VOST)', 'vostfr.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def MyshowSearchSerie():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = key_search_series + sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def MyshowSearchMovie():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = key_search_movies + sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showMovieGenres():
    oGui = cGui()

    # genre enlevés tous les films hs : Walt-Disney, Super_héros
    # arts-martiaux 4 films marche sur 150

    liste = []
    listegenre = ['action', 'animation', 'arts-martiaux', 'aventure', 'biopic', 'comédie', 'comédie-dramatique',
                  'comédie-musicale', 'drame', 'documentaire', 'epouvante_horreur', 'espionnage', 'famille',
                  'fantastique', 'musical', 'guerre', 'historique', 'policier', 'romance', 'science-fiction',
                  'thriller', 'western']

    # https://www1.hds.fm/film-genre/action
    for igenre in listegenre:
        liste.append([igenre.capitalize(), URL_MAIN + 'film-genre/' + igenre])

    for sTitle, sUrl in liste:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSerieGenres():
    oGui = cGui()
    liste = []
    listegenre = ['Action', 'Animation', 'Arts-martiaux', 'Aventure', 'Biopic', 'Comédie', 'Drame',
                  'Epouvante_horreur', 'Famille', 'Historique', 'Judiciaire', 'Médical', 'Policier',
                  'Romance', 'Science-fiction', 'Sport-event', 'Thriller', 'Western']

    # https://www1.hds.fm/serie-genre/Drame/
    for igenre in listegenre:
        urlgenre = igenre
        if igenre == 'judiciaire':
            urlgenre = 'judiciare'
        liste.append([igenre.capitalize(), URL_MAIN + 'serie-genre/' + urlgenre + '/'])

    for sTitle, sUrl in liste:

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovies(sSearch=''):
    oGui = cGui()
    oParser = cParser()

    bSearchMovie = False
    bSearchSerie = False
    if sSearch:

        sSearch = sSearch.replace('%20', ' ')

        if key_search_movies in sSearch:
            sSearch = sSearch.replace(key_search_movies, '')
            bSearchMovie = True
        if key_search_series in sSearch:
            sSearch = sSearch.replace(key_search_series, '')
            bSearchSerie = True
        sSearch2 = sSearch.replace('-', '').strip().lower()
        sUrl = URL_SEARCH[0] + sSearch2
        oRequest = cRequestHandler(sUrl)
        sHtmlContent = oRequest.request()

    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()

    sSearch2 = sSearch.replace('-', '').strip().lower()
    # ref thumb title
    sPattern = 'class="TPostMv">.+?href="([^"]*).+?src="([^"]*).+?center">([^<]*)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    itemss = 0

    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):

        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)
        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break

            itemss += 1

            sUrl2 = aEntry[0]
            sThumb = aEntry[1]
            sTitle = aEntry[2]

            if bSearchMovie:
                if ' saison ' in sTitle.lower():
                    continue
            if bSearchSerie:
                if ' saison ' not in sTitle.lower():
                    continue

            if sSearch and itemss > 4:  # 5 premiers résultats non filtrés en cas d'erreur du filtre
                s1 = sTitle.lower()
                if '-' in s1:
                    s1 = s1.split('-')[0]
                if '(' in s1:
                    s1 = s1.split('(')[0]
                s1 = s1.strip()
                if sSearch2 not in s1:
                    continue

            sDisplayTitle = sTitle.replace('-', '')
            if sSearch and not bSearchMovie and not bSearchSerie:
                if '/serie' in sUrl or ' saison ' in sTitle.lower():
                    sDisplayTitle = sDisplayTitle + ' [serie]'
                else:
                    sDisplayTitle = sDisplayTitle + ' [film]'

            if 'http' not in sUrl2:
                sUrl2 = URL_MAIN[:-1] + sUrl2

            if 'http' not in sThumb:
                sThumb = URL_MAIN[:-1] + sThumb

            # pour le debugage source avec bcpdechance d'etre hs
            # films didfficile a obtenir apres id= 18729
            # if  not ('/serie' in sUrl or ' saison ' in sTitle.lower()):
                # idmovie = get_id_int_Movie(sUrl2)
                # if idmovie  <= 18729:
                    # sDisplayTitle = sDisplayTitle + ' *'

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)

            if '/serie' in sUrl or ' saison ' in sTitle.lower():

                oGui.addTV(SITE_IDENTIFIER, 'ShowEpisodes', sDisplayTitle, '', sThumb, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showMovieLinks', sDisplayTitle, '', sThumb, '', oOutputParameterHandler)

        progress_.VSclose(progress_)

    if not sSearch:
        bNextPage, urlNextPage, sNumPage = __checkForNextPage(sHtmlContent)
        if (bNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', urlNextPage)
            oGui.addNext(SITE_IDENTIFIER, 'showMovies', 'Page ' + sNumPage, oOutputParameterHandler)

        oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()
    sNumberNext = ''
    sNumberMax = ''
    sNumPage = ''

    if '<a class="next"' not in sHtmlContent:
        return False, 'none', 'none'

    if 'class="end"' in sHtmlContent:
        sPattern = 'class="end".+?">(\d+)'
    else:
        sPattern = '(\d+)<.a>\s*<a\sclass="next"'

    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sNumberMax = aResult[1][0]

    sPattern = 'class="next.+?href="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        urlNextPage = aResult[1][0]  # minimum requis
        if 'htpp' not in urlNextPage:
            urlNextPage = URL_MAIN[:-1] + urlNextPage
        try:
            sNumberNext = re.search('/(\d+)/', urlNextPage).group(1)
        except:
            pass

        if sNumberNext:
            sNumPage = sNumberNext
            if sNumberMax:
                sNumPage = sNumPage + '/' + sNumberMax

        if urlNextPage:
            return True, urlNextPage, sNumPage

    return False, 'none', 'none'


def ShowEpisodes():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    if not 'saison' in sMovieTitle.lower():
        sPattern = 'saison-(\d+)'
        aResult = oParser.parse(sUrl, sPattern)
        if (aResult[0] == True):
            sMovieTitle = sMovieTitle + ' - Saison ' + aResult[1][0]

    sPattern = '<div class="Description">.*?>([^<]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sDesc = 'Hds Film'
    if (aResult[0] == True):
        sDesc = ('[I][COLOR grey]%s[/COLOR][/I] %s') % ('Synopsis :', cleanDesc(aResult[1][0]))

    sPattern = 'fa-play-circle-o">.+?(VOSTFR|VF)|id="(?:honey|yoyo)(?:\d+)"\s*href="([^"]+).+?title="([^"]+).+?data-rel="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    bfind = ""
    ValidEntry = ""

    if (aResult[0] == True):
        for aEntry in aResult[1]:
            if aEntry[0]:
                Slang = aEntry[0].replace('-tab', '').replace('"', '')
                bfind = True

            if bfind and aEntry[1]:
                ValidEntry = True
                sFirst_Url = aEntry[1]
                sEpisode = aEntry[2]
                sRel_Episode = aEntry[3]

                sDisplayTitle = sMovieTitle.replace('-', '') + ' ' + sEpisode + ' ' + Slang

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sUrl)
                oOutputParameterHandler.addParameter('sThumb', sThumb)
                oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle)
                oOutputParameterHandler.addParameter('sDesc', sDesc)
                oOutputParameterHandler.addParameter('sRel_Episode', sRel_Episode)
                oOutputParameterHandler.addParameter('sFirst_Url', sFirst_Url)
                oOutputParameterHandler.addParameter('sDisplayTitle', sDisplayTitle)

                oGui.addEpisode(SITE_IDENTIFIER, 'showSerieLinks', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)

    if not ValidEntry:
        oGui.addText(SITE_IDENTIFIER, '# Aucune vidéo trouvée #')

    oGui.setEndOfDirectory()


def showSerieLinks():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')
    sRel_Episode = oInputParameterHandler.getValue('sRel_Episode')
    sFirst_Url = oInputParameterHandler.getValue('sFirst_Url')
    sDisplayTitle1 = oInputParameterHandler.getValue('sDisplayTitle')

    oParser = cParser()
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div id="' + sRel_Episode + '" class="fullsfeature".*?<a (id="singh.*?<div style="height)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == False):
        # cas ou il n'y a qu'un seul lien  pas de référence  dans <div id="episodexx" class="fullsfeature">
        # le pattern est normalement hs
        if sFirst_Url:
            sUrl2 = sFirst_Url
            sHost = '[COLOR coral]' + GetHostname(sUrl2) + '[/COLOR]'

            sDisplayTitle = sDisplayTitle1 + ' ' + sHost
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('referer', sUrl)

            oGui.addLink(SITE_IDENTIFIER, 'showSerieHosters', sDisplayTitle, sThumb, sDesc, oOutputParameterHandler)

    if (aResult[0] == True):
        html = aResult[1][0]
        sPattern = 'href="([^"]+).*?aria-hidden'
        aResulturl = oParser.parse(html, sPattern)
        if (aResulturl[0] == True):
            for aEntry in aResulturl[1]:
                sUrl2 = aEntry
                sHost = GetHostname(sUrl2)
                if len(aResult[1]) == 1 and 'openload' in sUrl2:
                    oGui.addText(SITE_IDENTIFIER, '[COLOR skyblue] openload : site non sécurisé [/COLOR]')
                    continue

                if isblackhost(sUrl2):
                    continue

                if 'hqq.tv' in sUrl2:
                    continue

                if 'www' in sHost.lower():
                    sHost = GetHostname(sUrl2)

                sHost = '[COLOR coral]' + sHost + '[/COLOR]'
                sDisplayTitle = sDisplayTitle1 + ' ' + sHost

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sUrl2)
                oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                oOutputParameterHandler.addParameter('sDesc', sDesc)
                oOutputParameterHandler.addParameter('sThumb', sThumb)
                oOutputParameterHandler.addParameter('referer', sUrl)

                oGui.addLink(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovieLinks():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    oParser = cParser()
    sPattern = 'Synopsis.+?<p>([^<]*)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sDesc = 'Hds Film'
    if (aResult[0] == True):
        sDesc = ('[I][COLOR grey]%s[/COLOR][/I] %s') % ('Synopsis :', cleanDesc(aResult[1][0]))

    sPattern = '<a style=".+?cid="([^"]+).+?fa-play.+?i>([^<]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        for aEntry in aResult[1]:
            sUrl2 = aEntry[0]
            sHost = aEntry[1].strip().capitalize()
            # VSlog(sUrl2)
            if len(aResult[1]) == 1:
                if 'openload' in sHost.lower():
                    oGui.addText(SITE_IDENTIFIER, '[COLOR skyblue] openload : site non sécurisé [/COLOR]')
                    continue
                if 'oload' in sHost.lower():
                    oGui.addText(SITE_IDENTIFIER, '[COLOR skyblue] oload : site non sécurisé [/COLOR]')
                    continue

            if isblackhost(sUrl2):
                continue

            if 'hqq.tv' in sUrl2:
                continue

            if 'www' in sHost.lower():
                sHost = GetHostname(sUrl2)

            sDisplayTitle = sTitle + ' ' + '[COLOR coral]' + sHost + '[/COLOR]'

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('referer', sUrl)

            oGui.addLink(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, sThumb, sDesc, oOutputParameterHandler)
    oGui.setEndOfDirectory()


def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    sHosterUrl = sUrl
    oHoster = cHosterGui().checkHoster(sHosterUrl)
    if (oHoster != False):
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()


# teste id movie
def get_id_int_Movie(url):

    try:
        number = re.search('https.+?\/(\d+)', url).group(1)
        return int(number)
    except:
        return 20000
        pass
    return 20000


def GetHostname(url):

    try:
        if 'opsktp' in url:
            sHost = re.search('http.+?opsktp.+?\/([^\/]+)', url).group(1)

        elif 'www' not in url:
            sHost = re.search('http.*?\/\/([^.]*)', url).group(1)
        else:
            sHost = re.search('htt.+?\/\/(?:www).([^.]*)', url).group(1)
    except:
        sHost = url

    return sHost.capitalize()


def cleanDesc(sDesc):
    oParser = cParser()
    sPattern = '(Résumé.+?streaming Complet)'
    aResult = oParser.parse(sDesc, sPattern)

    if (aResult[0] == True):
        sDesc = sDesc.replace(aResult[1][0], '')

    list_comment = [':', 'en streaming', 'Voir Serie ']

    for s in list_comment:
        sDesc = sDesc.replace(s, '')

    return sDesc


def isblackhost(url):
    black_host = ['youflix', 'verystream', 'javascript', '4k-pl', 'ffsplayer', 'french-stream.ga', 'oload.stream','french-player.ga', 'streamango.com']

    urllower = url.lower()
    for host in black_host:
        if host.lower() in urllower:
            return True
    return False
