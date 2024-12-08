from shiny import ui
from algorithm.confmatrix import accuracy, mse, mae, r2, SVR_mae, SVR_mse, SVR_r2, RFR_mae ,RFR_mse,RFR_r2

# Define UI
app_ui = ui.page_fluid(
    ui.navset_tab(
        # Page 1
        ui.nav_panel(
            "Tennis Data",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_select(
                        "dataframe", "Select Dataframe", 
                        choices=["Session Summary", "Shot Stats", "Rally Stats", "Match Stats"]
                    ),
                    ui.input_select(
                        "var", "Select Variable", 
                        choices=["Shot Type", "Stroke", "Context", "Outcome"]
                    )
                ),
                
                    ui.navset_tab(
                        ui.nav_panel(
                            "Plot",
                            ui.output_plot("hist_plot")
                        ),
                        ui.nav_panel(
                            "Table",
                            ui.output_data_frame("data_table")
                        )
                    )
                
            )
        ),
        # Page 2
        ui.nav_panel(
            "Algorithms",
            ui.h3(f"Accuracy: {accuracy * 100:.2f}"),
            ui.output_plot("conf_matrix_heatmap"),
                               
                ui.navset_tab(
                        ui.nav_panel(
                            "Logistic Model Evaluation",
                            ui.p(f"Means Squared Error: {mse:.2f}"),
                            ui.p(f"Means Absolute Error: {mae:.2f}"),
                            ui.p(f"R-squared: {r2:.2f}")
                        ),
                        ui.nav_panel(
                            "SVR Model Evaluation",
                            ui.p(f"Means Squared Error: {SVR_mse:.2f}"),
                            ui.p(f"Means Absolute Error: {SVR_mae:.2f}"),
                            ui.p(f"R-squared: {SVR_r2:.2f}")
                        ),
                        ui.nav_panel(
                            "Random Forest Regressor Model Evaluation",
                            ui.p(f"Means Squared Error: {RFR_mse:.2f}"),
                            ui.p(f"Means Absolute Error: {RFR_mae:.2f}"),
                            ui.p(f"R-squared: {RFR_r2:.2f}")
                        )
                )
            
        ),
        ui.nav_panel(
            "Exploratory",
            ui.h3(f"Decision Tree of Shot Statistics"),
            ui.output_plot("decision_tree_plot"),
            ui.output_plot("player_bar_chart")
                
            
        )
    )
)