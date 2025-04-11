def predict_ensemble(new_data, xgb_model, sj_sarima_model, iq_sarima_model, ensemble_config):
    """
    Make predictions using the optimized ensemble model.
    
    Parameters:
    -----------
    new_data : DataFrame
        New data for predictions with the same features as the training data
    xgb_model : XGBoost model object
        Trained XGBoost model
    sj_sarima_model, iq_sarima_model : SARIMAX results objects
        Trained SARIMA models for each city
    ensemble_config : dict
        Configuration with weights for each city
        
    Returns:
    --------
    DataFrame with predictions
    """
    # Make predictions with XGBoost
    xgb_preds = xgb_model.predict(new_data.drop(['city', 'week_start_date'], axis=1, errors='ignore'))
    
    # Prepare results DataFrame
    results = pd.DataFrame({
        'city': new_data['city'],
        'week_start_date': new_data['week_start_date'],
        'xgb_predicted': xgb_preds
    })
    
    # Get SARIMA predictions for each city
    # This would depend on how you structure your forecast periods
    # For simplicity, this is a placeholder
    # In practice, you'd need to set up the forecast periods correctly
    
    # Apply city-specific weights to get ensemble predictions
    results['ensemble_predicted'] = results.apply(
        lambda row: ensemble_config['sj_weights']['xgb'] * row['xgb_predicted'] + 
                   ensemble_config['sj_weights']['sarima'] * sarima_pred if row['city'] == 'sj' else
                   ensemble_config['iq_weights']['xgb'] * row['xgb_predicted'] + 
                   ensemble_config['iq_weights']['sarima'] * sarima_pred,
        axis=1
    )
    
    return results
