import pandas as pd

def prepare_sample_data(self):
    """
    Create a dataset based on the provided Ayurvedic and Medicinal Plants data
    """
    # Dataset from the problem statement
    data = {
        'plant_name': [
            'Tulsi', 'Ginger', 'Licorice', 'Turmeric', 'Neem', 
            'Licorice', 'Ginger', 'Licorice', 'Ginger', 'Ginger', 
            'Brahmi', 'Fenugreek', 'Neem', 'Licorice', 'Amla', 
            'Neem', 'Fenugreek', 'Nimba', 'Ashwagandha', 'Amla'
        ],
        'ayurvedic_name': [
            'Tulasi', 'Adrak', 'Yashtimadhu', 'Haridra', 'Nimba', 
            'Yashtimadhu', 'Adrak', 'Yashtimadhu', 'Adrak', 'Adrak', 
            'Brahmi', 'Methi', 'Nimba', 'Yashtimadhu', 'Amla', 
            'Nimba', 'Mehti', 'Nimba', 'Ashwagandha', 'Amla'
        ],
        'seasonality': [
            'Autumn', 'Autumn', 'Summer', 'Monsoon', 'Monsoon', 
            'Monsoon', 'Spring', 'Winter', 'Spring', 'Winter', 
            'Monsoon', 'Monsoon', 'Spring', 'Spring', 'Winter', 
            'Autumn', 'Winter', 'Spring', 'Spring', 'Summer'
        ],
        'health_benefits': [
            ['Skin Health', 'Immunity Booster'], 
            ['Skin Health', 'Digestive Aid'], 
            ['Skin Health', 'Digestive Aid'], 
            ['Hair Strengthening', 'Anti-inflammatory'], 
            ['Blood Purifier', 'Skin Health'], 
            ['Blood Purifier'], 
            ['Antioxidant', 'Digestive Aid'], 
            ['Digestive Aid'], 
            ['Skin Health'], 
            ['Blood Purifier'], 
            ['Hair Strengthening'], 
            ['Antioxidant'], 
            ['Stress Relief'], 
            ['Antioxidant'], 
            ['Blood Purifier'], 
            ['Immunity Booster'], 
            ['Hair Strengthening'], 
            ['Immunity Booster'], 
            ['Skin Health'], 
            ['Immunity Booster']
        ],
        'image': [
            'tulsi.jpg', 'ginger.jpg', 'licorice.jpg', 'turmeric.jpg', 'neem.jpg', 
            'licorice_blood.jpg', 'ginger_spring.jpg', 'licorice_winter.jpg', 
            'ginger_skin.jpg', 'ginger_purifier.jpg', 'brahmi.jpg', 
            'fenugreek.jpg', 'neem_stress.jpg', 'licorice_antioxidant.jpg', 
            'amla_purifier.jpg', 'neem_immunity.jpg', 'fenugreek_hair.jpg', 
            'neem_immunity2.jpg', 'ashwagandha.jpg', 'amla_immunity.jpg'
        ]
    }
    
    # Return the dataframe with the new data
    return pd.DataFrame(data)
