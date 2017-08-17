/*
A KBase module: kb_stringtie
*/

module kb_stringtie {
    /* A boolean - 0 for false, 1 for true.
        @range (0, 1)
    */
    typedef int boolean;

    /* An X/Y/Z style reference
    */
    typedef string obj_ref;

    /*  
        required params:
        alignment_object_ref: Alignment or AlignmentSet object reference
        workspace_name: the name of the workspace it gets saved to
        expression_set_suffix: suffix append to expression set object name
        expression_suffix: suffix append to expression object name
        mode: one of ['normal', 'merge', 'novel_isoform']

        optional params:
        num_threads: number of processing threads
        junction_base: junctions that don't have spliced reads
        junction_coverage: junction coverage
        disable_trimming: disables trimming at the ends of the assembled transcripts
        min_locus_gap_sep_value: minimum locus gap separation value
        ballgown_mode: enables the output of Ballgown input table files
        skip_reads_with_no_ref: reads with no reference will be skipped
        maximum_fraction: maximum fraction of muliple-location-mapped reads
        label: prefix for the name of the output transcripts
        min_length: minimum length allowed for the predicted transcripts
        min_read_coverage: minimum input transcript coverage
        min_isoform_abundance: minimum isoform abundance

        ref: http://ccb.jhu.edu/software/stringtie/index.shtml?t=manual
    */
    typedef structure {
        obj_ref alignment_object_ref;
        string workspace_name;
        string expression_set_suffix;
        string expression_suffix;
        string mode;

        int num_threads;
        int junction_base;
        float junction_coverage;
        boolean disable_trimming;
        int min_locus_gap_sep_value;
        boolean ballgown_mode;
        boolean skip_reads_with_no_ref;
        float maximum_fraction;
        string label;
        int min_length;
        float min_read_coverage;
        float min_isoform_abundance;
    } StringTieInput;

    /*
        result_directory: folder path that holds all files generated by run_stringtie
        expression_obj_ref: generated Expression/ExpressionSet object reference
        exprMatrix_FPKM/TPM_ref: generated FPKM/TPM ExpressionMatrix object reference 
        report_name: report name generated by KBaseReport
        report_ref: report reference generated by KBaseReport
    */
    typedef structure{
        string result_directory;
        obj_ref expression_obj_ref;
        obj_ref exprMatrix_FPKM_ref;
        obj_ref exprMatrix_TPM_ref;
        string report_name;
        string report_ref;
    }StringTieResult;

    /*  
        run_stringtie_app: run StringTie app

        ref: http://ccb.jhu.edu/software/stringtie/index.shtml?t=manual
    */
    funcdef run_stringtie_app(StringTieInput params)
        returns (StringTieResult returnVal) authentication required;
};
