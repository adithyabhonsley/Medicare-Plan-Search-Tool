import json

# Get all the titles
titles = "pbp_a_hnumber	pbp_a_plan_identifier	segment_id	pbp_a_ben_cov	pbp_a_plan_type	orgtype	bid_id	version	pbp_a_contract_partd_flag	pbp_a_platino_flag	pbp_a_snp_pct	pbp_a_vbid_indicator	pbp_a_partd_model_flag	pbp_a_last_data_entry_date	pbpver	pbp_a_ready_for_upload_date_tm	pbp_a_BPT_MA_date_time	pbp_a_BPT_PD_date_time	pbp_a_BPT_MSA_date_time	pbp_a_BPT_ESRD_date_time	pbp_a_upload_date_time	pbp_a_org_name	pbp_a_org_marketing_name	pbp_a_org_website	pbp_a_plan_name	pbp_a_org_type	pbp_a_plan_type	pbp_a_network_flag	pbp_a_ben_cov	pbp_a_hospice_care_yn	pbp_a_service_area	pbp_a_contract_number	pbp_a_plan_identifier	pbp_a_segment_id	pbp_a_contract_period	pbp_a_plan_geog_name	pbp_a_segment_name	pbp_a_eghp_yn	pbp_a_est_memb	pbp_a_continue_yn	pbp_a_continue_costshare_yn	pbp_a_platino_yn	pbp_a_special_need_flag	pbp_a_special_need_plan_type	pbp_a_snp_institutional_type	pbp_a_dsnp_zerodollar	pbp_a_snp_cond	pbp_a_snp_state_cvg_yn	pbp_a_pharmacy_website	pbp_a_formulary_web_addr	pbp_a_phys_web_addr	pbp_a_curmbr_phone	pbp_a_curmbr_phone_ext	pbp_a_curmbr_loc_phone	pbp_a_curmbr_loc_phone_ext	pbp_a_prombr_phone	pbp_a_prombr_phone_ext	pbp_a_prombr_loc_phone	pbp_a_prombr_loc_phone_ext	pbp_a_pd_curmbr_phone	pbp_a_pd_curmbr_phone_ext	pbp_a_pd_curmbr_loc_phone	pbp_a_pd_curmbr_loc_phone_ext	pbp_a_pd_prombr_phone	pbp_a_pd_prombr_phone_ext	pbp_a_pd_prombr_loc_phone	pbp_a_pd_prombr_loc_phone_ext	pbp_a_ttytdd_curmbr_phone	pbp_a_ttytdd_curmbr_phone_ext	pbp_a_ttytdd_cur_loc_phone	pbp_a_ttytdd_cur_loc_phone_ext	pbp_a_ttytdd_prombr_phone	pbp_a_ttytdd_prombr_phone_ext	pbp_a_ttytdd_pro_loc_phone	pbp_a_ttytdd_pro_loc_phone_ext	pbp_a_pd_ttytdd_curmbr_phone	pbp_a_pd_ttytdd_curmbr_phn_ext	pbp_a_pd_ttytdd_cur_loc_phone	pbp_a_pd_ttytdd_cur_loc_phn_ex	pbp_a_pd_ttytdd_prombr_phone	pbp_a_pd_ttytdd_prombr_phn_ext	pbp_a_pd_ttytdd_pro_loc_phone	pbp_a_pd_ttytdd_pro_loc_phn_ex	pbp_a_ffs_bid_b_yn	pbp_a_ffs_bid_b_auth_yn	pbp_a_ffs_bid_b_auth_cats	pbp_a_ffs_bid_b_ref_yn	pbp_a_ffs_bid_b_ref_cats	pbp_a_ffs_bid_c_yn	pbp_a_ffs_bid_c_auth_yn	pbp_a_ffs_bid_c_auth_cats	pbp_a_ffs_bid_c_ref_yn	pbp_a_ffs_bid_c_ref_cats	pbp_a_ffs_bid_d_yn	pbp_a_tier_yn	pbp_a_tier_bendesc_bens	pbp_a_tier_mc_bendesc_cats	pbp_a_tier_nmc_bendesc_cats"

# Split all the titles by a tab-space to get individual titles
titles = titles.split("	")

# List of all the titles we need
required_titles = ["pbp_a_org_marketing_name",
                   "pbp_a_plan_name", "pbp_a_org_website", "pbp_a_plan_geog_name"]


# Print all the indexes of required titles to use later
for i in range(len(titles)):
    if (titles[i] in required_titles):
        print(titles[i], i)

# Open the medicare text file and read all lines
f = open("./medicare_plans.txt", "r")
l = f.readlines()
f.close()

# Create a map to store all data and export as JSON 
m = {}

# Read each line and choose selected fields
for i in range(len(l)):
    line = l[i]
    line = line.split("	")
    temp = {}
    temp["Insurance Carrier"] = line[22]
    temp["Insurance Plan"] = line[24]
    temp["Pharmacy Website"] = line[23]
    temp["Geographic Area"] = line[35]
    m[line[6]] = temp


# Write the map to JSON file. Make sure to copy JSON file to the folder src/
j = json.dumps(m, indent=4)

f = open('medicare.json', 'w')
print(j, file=f)
f.close()
