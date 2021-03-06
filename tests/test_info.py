#!/usr/bin/env python

import unittest

import mlbgame

from datetime import datetime


class TestInfo(unittest.TestCase):

    def test_league(self):
        league = mlbgame.league()
        self.assertEqual(league.aws_club_slug, '')
        self.assertEqual(league.club, 'mlb')
        self.assertEqual(league.club_common_name, 'MLB')
        self.assertEqual(league.club_common_url, 'MLB.com')
        self.assertEqual(league.club_full_name, 'Major League Baseball')
        self.assertEqual(league.club_id, 1)
        self.assertEqual(league.club_spanish_name, 'Las Grandes Ligas')
        self.assertEqual(league.dc_site, 'mlb.mlb')
        self.assertEqual(league.display_code, 'mlb')
        self.assertEqual(league.division, '')
        self.assertEqual(league.es_track_code, 'mlbcomes')
        self.assertEqual(league.esp_common_name, 'Las Mayores')
        self.assertEqual(league.esp_common_url, 'LasMayores.com')
        self.assertEqual(league.facebook, 'MLB')
        self.assertEqual(league.facebook_es, 'lasmayores')
        self.assertEqual(league.fanphotos_url, '')
        self.assertEqual(league.fb_app_id, 5768707450)
        self.assertEqual(league.field, '')
        self.assertEqual(league.google_tag_manager, 'GTM-TGJ9RZ')
        self.assertEqual(league.googleplus_id, 109783101935210076456)
        self.assertEqual(league.historical_team_code, '')
        self.assertEqual(league.id, 35003)
        self.assertEqual(league.instagram, 'mlb')
        self.assertEqual(league.instagram_id, 52762453)
        self.assertEqual(league.league, 'Major')
        self.assertEqual(league.location, '')
        self.assertEqual(league.medianet_id, 8)
        self.assertEqual(league.mobile_es_url, 'http://m.es.mlb.com')
        self.assertEqual(league.mobile_short_code, 'N/A')
        self.assertEqual(league.mobile_url, 'http://m.mlb.com')
        self.assertEqual(league.mobile_url_base, 'mlb.com')
        self.assertEqual(league.name_display_long, 'Major League Baseball')
        self.assertEqual(league.name_display_short, 'MLB')
        self.assertEqual(league.newsletter_category_id, 1)
        self.assertEqual(league.newsletter_group_id, 1)
        self.assertEqual(league.photostore_url, 'https://photostore.mlb.com/')
        self.assertEqual(league.pinterest, 'MLBOfficial')
        self.assertEqual(league.pinterest_verification, '51e25f1d2a798834eedbca4dfd4c8008')
        self.assertEqual(league.pressbox_title, 'MLBpressbox.com')
        self.assertEqual(league.pressbox_url, 'mlbpressbox.com')
        self.assertEqual(league.primary, '#000063')
        self.assertEqual(league.primary_link, '#0000cc')
        self.assertEqual(league.secondary, '#ce0000')
        self.assertEqual(league.snapchat, 'mlb')
        self.assertEqual(league.snapchat_es, 'lasmayores')
        self.assertEqual(league.team_code, 'mlb')
        self.assertEqual(league.team_id, '')
        self.assertEqual(league.tertiary, '#cccccc')
        self.assertEqual(league.timezone, '')
        self.assertEqual(league.track_code, 'mlbcom08')
        self.assertEqual(league.track_code_dev, 'devmlbcom')
        self.assertEqual(league.track_filter, 'mlb')
        self.assertEqual(league.tumblr, 'mlb')
        self.assertEqual(league.twitter, 'mlb')
        self.assertEqual(league.twitter_es, 'LasMayores')
        self.assertEqual(league.url_cache, 'mlb.mlb.com')
        self.assertEqual(league.url_esp, '/es/index.jsp?c_id=mlb')
        self.assertEqual(league.url_prod, 'www.mlb.com')
        self.assertEqual(league.vine, 908066689910976512)
        self.assertEqual(league.__str__(), 'Major League Baseball (MLB)')

    def test_league_empty(self):
        mlbgame.data.PROPERTY_URL = 'http://mlb.mlb.com/properties/mlb_properties'
        self.assertRaises(ValueError, lambda: mlbgame.league())
        mlbgame.data.PROPERTY_URL = 'http://mlb.mlb.com/properties/mlb_properties.xml'

    def test_teams(self):
        teams = mlbgame.teams()
        for team in teams:
            self.assertIsInstance(team.address, str)
            self.assertIsInstance(team.aws_club_slug, str)
            self.assertIsInstance(team.city, str)
            self.assertIsInstance(team.club, str)
            self.assertIsInstance(team.club_common_name, str)
            self.assertIsInstance(team.club_common_url, str)
            self.assertIsInstance(team.club_full_name, str)
            self.assertIsInstance(team.club_id, int)
            self.assertIsInstance(team.club_spanish_name, str)
            self.assertIsInstance(team.country, str)
            self.assertIsInstance(team.dc_site, str)
            self.assertIsInstance(team.display_code, str)
            self.assertIsInstance(team.division, str)
            self.assertIsInstance(team.es_track_code, str)
            self.assertIsInstance(team.esp_common_name, str)
            self.assertIsInstance(team.esp_common_url, str)
            self.assertIsInstance(team.facebook, str)
            self.assertIsInstance(team.fanphotos_url, str)
            self.assertIsInstance(team.fb_app_id, int)
            self.assertIsInstance(team.field, str)
            self.assertIsInstance(team.google_tag_manager, str)
            try:
                self.assertIsInstance(team.googleplus_id, long)
            except NameError:
                self.assertIsInstance(team.googleplus_id, int)
            self.assertIsInstance(team.historical_team_code, str)
            self.assertIsInstance(team.id, int)
            self.assertIsInstance(team.instagram, str)
            self.assertIsInstance(team.instagram_id, int)
            self.assertIsInstance(team.league, str)
            self.assertIsInstance(team.location, str)
            self.assertIsInstance(team.medianet_id, int)
            self.assertIsInstance(team.mobile_es_url, str)
            self.assertIsInstance(team.mobile_short_code, (int, str))
            self.assertIsInstance(team.mobile_url, str)
            self.assertIsInstance(team.mobile_url_base, str)
            self.assertIsInstance(team.name_display_long, str)
            self.assertIsInstance(team.name_display_short, str)
            self.assertIsInstance(team.newsletter_category_id, int)
            self.assertIsInstance(team.newsletter_group_id, int)
            self.assertIsInstance(team.phone, str)
            self.assertIsInstance(team.photostore_url, str)
            self.assertIsInstance(team.pinterest, str)
            self.assertIsInstance(team.pinterest_verification, str)
            self.assertIsInstance(team.pressbox_title, str)
            self.assertIsInstance(team.pressbox_url, str)
            self.assertIsInstance(team.primary, str)
            self.assertIsInstance(team.primary_link, str)
            self.assertIsInstance(team.postal_code, (int, str))
            self.assertIsInstance(team.secondary, str)
            self.assertIsInstance(team.shop_entry_code, int)
            self.assertIsInstance(team.snapchat, str)
            self.assertIsInstance(team.state_province, str)
            self.assertIsInstance(team.team_code, str)
            self.assertIsInstance(team.team_id, int)
            self.assertIsInstance(team.tertiary, str)
            self.assertIsInstance(team.timezone, str)
            self.assertIsInstance(team.track_code, str)
            self.assertIsInstance(team.track_code_dev, str)
            self.assertIsInstance(team.track_filter, str)
            self.assertIsInstance(team.tumblr, str)
            self.assertIsInstance(team.twitter, str)
            self.assertIsInstance(team.twitter_es, str)
            self.assertIsInstance(team.url_cache, str)
            self.assertIsInstance(team.url_esp, str)
            self.assertIsInstance(team.url_prod, str)
            self.assertIsInstance(team.venue_id, int)
            self.assertIsInstance(team.vine, (int, str))
            self.assertIsInstance(team.youtube, str)
        team = teams[17]
        self.assertEqual(team.address, '120-01 Roosevelt Avenue')
        self.assertEqual(team.aws_club_slug, 'mets')
        self.assertEqual(team.city, 'Corona')
        self.assertEqual(team.club, 'nym')
        self.assertEqual(team.club_common_name, 'Mets')
        self.assertEqual(team.club_common_url, 'mets.com')
        self.assertEqual(team.club_full_name, 'New York Mets')
        self.assertEqual(team.club_id, 20)
        self.assertEqual(team.club_spanish_name, 'Los Mets de Nueva York')
        self.assertEqual(team.country, 'USA')
        self.assertEqual(team.dc_site, 'mets.mlb')
        self.assertEqual(team.display_code, 'nym')
        self.assertEqual(team.division, 'East')
        self.assertEqual(team.es_track_code, 'mlbmetses')
        self.assertEqual(team.esp_common_name, 'Mets')
        self.assertEqual(team.esp_common_url, 'losmets.com')
        self.assertEqual(team.facebook, 'Mets')
        self.assertEqual(team.facebook_es, 284924024933471)
        self.assertEqual(team.fanphotos_url, '')
        self.assertEqual(team.fb_app_id, 94421890077)
        self.assertEqual(team.field, 'Citi Field')
        self.assertEqual(team.google_tag_manager, 'GTM-WGDHL4')
        self.assertEqual(team.googleplus_id, 111969268508366177113)
        self.assertEqual(team.historical_team_code, 'NYN')
        self.assertEqual(team.id, 36018)
        self.assertEqual(team.instagram, 'mets')
        self.assertEqual(team.instagram_id, 50927135)
        self.assertEqual(team.league, 'National')
        self.assertEqual(team.location, 'New York')
        self.assertEqual(team.medianet_id, 25)
        self.assertEqual(team.mobile_es_url, 'http://m.es.mets.mlb.com')
        self.assertEqual(team.mobile_short_code, 48593)
        self.assertEqual(team.mobile_url, 'http://m.mets.mlb.com')
        self.assertEqual(team.mobile_url_base, 'mets.mlb.com')
        self.assertEqual(team.name_display_long, 'The New York Mets')
        self.assertEqual(team.name_display_short, 'NY Mets')
        self.assertEqual(team.newsletter_category_id, 21)
        self.assertEqual(team.newsletter_group_id, 29)
        self.assertEqual(team.phone, '(718) 507-6387')
        self.assertEqual(team.photostore_url, 'https://photostore.mlb.com/collections/new-york-mets')
        self.assertEqual(team.pinterest, 'metsbaseball')
        self.assertEqual(team.pinterest_verification, 'a7f4172888a65c72793112432c061cc3')
        self.assertEqual(team.pressbox_title, 'MetsPressbox.com')
        self.assertEqual(team.pressbox_url, 'metspressbox.com')
        self.assertEqual(team.primary, '#003581')
        self.assertEqual(team.primary_link, '#ff5910')
        self.assertEqual(team.postal_code, 11368)
        self.assertEqual(team.secondary, '#ff5731')
        self.assertEqual(team.shop_entry_code, 1452359)
        self.assertEqual(team.snapchat, 'mets')
        self.assertEqual(team.state_province, 'NY')
        self.assertEqual(team.team_code, 'nyn')
        self.assertEqual(team.team_id, 121)
        self.assertEqual(team.tertiary, '#e6e6e6')
        self.assertEqual(team.timezone, 'ET')
        self.assertEqual(team.track_code, 'mlbmets')
        self.assertEqual(team.track_code_dev, 'devmlbnewyork')
        self.assertEqual(team.track_filter, 'newyork,mets')
        self.assertEqual(team.tumblr, 'mets')
        self.assertEqual(team.twitter, 'Mets')
        self.assertEqual(team.twitter_es, 'LosMets')
        self.assertEqual(team.url_cache, 'newyork.mets.mlb.com')
        self.assertEqual(team.url_esp, '/es/index.jsp?c_id=nym')
        self.assertEqual(team.url_prod, 'mets.mlb.com')
        self.assertEqual(team.venue_id, 3289)
        self.assertEqual(team.vine, 929089218578374656)
        self.assertEqual(team.youtube, 'UCgIMbGazP0uBDy9JVCqBUaA')
        

    def test_roster(self):
        roster = mlbgame.roster(121)
        self.assertIsInstance(roster.last_update, datetime)
        self.assertIsInstance(roster.roster, list)
        for player in roster.roster:
            self.assertIsInstance(player.bats, str)
            self.assertIsInstance(player.birth_date, str)
            self.assertIsInstance(player.college, str)
            self.assertIsInstance(player.end_date, str)
            self.assertIsInstance(player.height_feet, int)
            self.assertIsInstance(player.height_inches, int)
            self.assertIsInstance(player.jersey_number, (int, str))
            self.assertIsInstance(player.name_display_first_last, str)
            self.assertIsInstance(player.name_display_last_first, str)
            self.assertIsInstance(player.name_first, str)
            self.assertIsInstance(player.name_full, str)
            self.assertIsInstance(player.name_last, str)
            self.assertIsInstance(player.name_use, str)
            self.assertIsInstance(player.player_id, int)
            self.assertIsInstance(player.position_txt, str)
            self.assertIsInstance(player.primary_position, int)
            self.assertIsInstance(player.pro_debut_date, str)
            self.assertIsInstance(player.start_date, str)
            self.assertIsInstance(player.starter_sw, str)
            self.assertIsInstance(player.status_code, str)
            self.assertIsInstance(player.team_abbrev, str)
            self.assertIsInstance(player.team_code, str)
            self.assertIsInstance(player.team_id, int)
            self.assertIsInstance(player.team_name, str)
            self.assertIsInstance(player.throws, str)
            self.assertIsInstance(player.weight, int)
            self.assertEqual(player.team_abbrev, 'NYM')
            self.assertEqual(player.team_code, 'nyn')
            self.assertEqual(player.team_id, 121)
            self.assertEqual(player.team_name, 'New York Mets')

    def test_standings(self):
        standings = mlbgame.standings()
        self.assertEqual(standings.standings_schedule_date, 'standings_schedule_date')
        self.assertIsInstance(standings.last_update, datetime)
        self.assertIsInstance(standings.divisions, list)
        for division in standings.divisions:
            self.assertIsInstance(division.name, str)
            self.assertIsInstance(division.teams, list)
            for team in division.teams:
                self.assertIsInstance(team.away, str)
                self.assertIsInstance(team.clinched_sw, str)
                self.assertIsInstance(team.division, str)
                self.assertIsInstance(team.division_champ, str)
                self.assertIsInstance(team.division_id, int)
                self.assertIsInstance(team.division_odds, float)
                self.assertIsInstance(team.elim, (str, int))
                self.assertIsInstance(team.elim_wildcard, (str, int))
                self.assertIsInstance(team.extra_inn, str)
                self.assertIsInstance(team.file_code, str)
                self.assertIsInstance(team.gb, (str, float))
                self.assertIsInstance(team.gb_wildcard, (str, float))
                self.assertIsInstance(team.home, str)
                self.assertIsInstance(team.interleague, str)
                self.assertIsInstance(team.is_wildcard_sw, str)
                self.assertIsInstance(team.l, int)
                self.assertIsInstance(team.last_ten, str)
                self.assertIsInstance(team.one_run, str)
                self.assertIsInstance(team.opp_runs, int)
                self.assertIsInstance(team.pct, float)
                self.assertIsInstance(team.place, int)
                self.assertIsInstance(team.playoff_odds, float)
                self.assertIsInstance(team.playoff_points_sw, str)
                self.assertIsInstance(team.playoffs_flag_milb, str)
                self.assertIsInstance(team.playoffs_flag_mlb, str)
                self.assertIsInstance(team.playoffs_sw, str)
                self.assertIsInstance(team.points, str)
                self.assertIsInstance(team.runs, int)
                self.assertIsInstance(team.sit_code, str)
                self.assertIsInstance(team.streak, str)
                self.assertIsInstance(team.team_abbrev, str)
                self.assertIsInstance(team.team_full, str)
                self.assertIsInstance(team.team_id, int)
                self.assertIsInstance(team.team_short, str)
                self.assertIsInstance(team.vs_central, str)
                self.assertIsInstance(team.vs_division, str)
                self.assertIsInstance(team.vs_east, str)
                self.assertIsInstance(team.vs_left, str)
                self.assertIsInstance(team.vs_right, str)
                self.assertIsInstance(team.vs_west, str)
                self.assertIsInstance(team.w, int)
                self.assertIsInstance(team.wild_card, str)
                self.assertIsInstance(team.wildcard_odds, float)
                self.assertIsInstance(team.x_wl, str)
                self.assertIsInstance(team.x_wl_seas, str)

    def test_standings_historical(self):
        date = datetime(2016, 6, 1)
        standings = mlbgame.standings(date)
        self.assertEqual(standings.standings_schedule_date, 'historical_standings_schedule_date')
        self.assertIsInstance(standings.last_update, datetime)
        self.assertIsInstance(standings.divisions, list)
        for division in standings.divisions:
            self.assertIsInstance(division.name, str)
            self.assertIsInstance(division.teams, list)
            if division.name == 'NL West':
                d = division
            for team in division.teams:
                self.assertIsInstance(team.away, str)
                self.assertIsInstance(team.clinched_sw, str)
                self.assertIsInstance(team.division, str)
                self.assertIsInstance(team.division_champ, str)
                self.assertIsInstance(team.division_id, int)
                self.assertIsInstance(team.division_odds, float)
                self.assertIsInstance(team.elim, (str, int))
                self.assertIsInstance(team.elim_wildcard, (str, int))
                self.assertIsInstance(team.extra_inn, str)
                self.assertIsInstance(team.file_code, str)
                self.assertIsInstance(team.gb, (str, float))
                self.assertIsInstance(team.gb_wildcard, (str, float))
                self.assertIsInstance(team.home, str)
                self.assertIsInstance(team.interleague, str)
                self.assertIsInstance(team.is_wildcard_sw, str)
                self.assertIsInstance(team.l, int)
                self.assertIsInstance(team.last_ten, str)
                self.assertIsInstance(team.one_run, str)
                self.assertIsInstance(team.opp_runs, int)
                self.assertIsInstance(team.pct, float)
                self.assertIsInstance(team.place, int)
                self.assertIsInstance(team.playoff_odds, float)
                self.assertIsInstance(team.playoff_points_sw, str)
                self.assertIsInstance(team.playoffs_flag_milb, str)
                self.assertIsInstance(team.playoffs_flag_mlb, str)
                self.assertIsInstance(team.playoffs_sw, str)
                self.assertIsInstance(team.points, str)
                self.assertIsInstance(team.runs, int)
                self.assertIsInstance(team.sit_code, str)
                self.assertIsInstance(team.streak, str)
                self.assertIsInstance(team.team_abbrev, str)
                self.assertIsInstance(team.team_full, str)
                self.assertIsInstance(team.team_id, int)
                self.assertIsInstance(team.team_short, str)
                self.assertIsInstance(team.vs_central, str)
                self.assertIsInstance(team.vs_division, str)
                self.assertIsInstance(team.vs_east, str)
                self.assertIsInstance(team.vs_left, str)
                self.assertIsInstance(team.vs_right, str)
                self.assertIsInstance(team.vs_west, str)
                self.assertIsInstance(team.w, int)
                self.assertIsInstance(team.wild_card, str)
                self.assertIsInstance(team.wildcard_odds, float)
                self.assertIsInstance(team.x_wl, str)
                self.assertIsInstance(team.x_wl_seas, str)
                if team.file_code == 'sf':
                    t = team
        division = d
        self.assertEqual(division.name, 'NL West')
        team = t
        self.assertEqual(team.away, '17-11')
        self.assertEqual(team.clinched_sw, 'N')
        self.assertEqual(team.division, 'National League West')
        self.assertEqual(team.division_champ, 'Y')
        self.assertEqual(team.division_id, 203)
        self.assertEqual(team.division_odds, 54.4)
        self.assertEqual(team.elim, '-')
        self.assertEqual(team.elim_wildcard, '')
        self.assertEqual(team.extra_inn, '4-3')
        self.assertEqual(team.file_code, 'sf')
        self.assertEqual(team.gb, '-')
        self.assertEqual(team.gb_wildcard, '')
        self.assertEqual(team.home, '16-11')
        self.assertEqual(team.interleague, '1-2')
        self.assertEqual(team.is_wildcard_sw, 'Y')
        self.assertEqual(team.l, 22)
        self.assertEqual(team.last_ten, '0-0')
        self.assertEqual(team.one_run, '12-6')
        self.assertEqual(team.opp_runs, 220)
        self.assertEqual(team.pct, .6)
        self.assertEqual(team.place, 1)
        self.assertEqual(team.playoff_odds, 77.1)
        self.assertEqual(team.playoff_points_sw, 'N')
        self.assertEqual(team.playoffs_flag_milb, '')
        self.assertEqual(team.playoffs_flag_mlb, '')
        self.assertEqual(team.playoffs_sw, 'N')
        self.assertEqual(team.points, '')
        self.assertEqual(team.runs, 242)
        self.assertEqual(team.sit_code, 'h0')
        self.assertEqual(team.streak, 'L1')
        self.assertEqual(team.team_abbrev, 'SF')
        self.assertEqual(team.team_full, 'San Francisco Giants')
        self.assertEqual(team.team_id, 137)
        self.assertEqual(team.team_short, 'San Francisco')
        self.assertEqual(team.vs_central, '6-3')
        self.assertEqual(team.vs_division, '22-12')
        self.assertEqual(team.vs_east, '4-5')
        self.assertEqual(team.vs_left, '11-8')
        self.assertEqual(team.vs_right, '22-14')
        self.assertEqual(team.vs_west, '22-12')
        self.assertEqual(team.w, 33)
        self.assertEqual(team.wild_card, 'N')
        self.assertEqual(team.wildcard_odds, 22.7)
        self.assertEqual(team.x_wl, '30-25')
        self.assertEqual(team.x_wl_seas, '88-74')

    def test_injury(self):
        injury = mlbgame.injury(121)
        self.assertIsInstance(injury.last_update, datetime)
        self.assertIsInstance(injury.injuries, list)
        for player in injury.injuries:
            self.assertIsInstance(player.display_ts, str)
            self.assertIsInstance(player.due_back, str)
            self.assertIsInstance(player.injury_desc, str)
            self.assertIsInstance(player.injury_status, str)
            self.assertIsInstance(player.injury_update, str)
            self.assertIsInstance(player.insert_ts, str)
            self.assertIsInstance(player.league_id, int)
            self.assertIsInstance(player.name_first, str)
            self.assertIsInstance(player.name_last, str)
            self.assertIsInstance(player.player_id, int)
            self.assertIsInstance(player.position, str)
            self.assertIsInstance(player.team_id, int)
            self.assertIsInstance(player.team_name, str)
            self.assertEqual(player.team_id, 121)
            self.assertEqual(player.team_name, 'Mets')
