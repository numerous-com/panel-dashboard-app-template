import panel as pn
import pandas as pd
import seaborn as sns
from perspective import PerspectiveViewer
import hvplot.pandas

# Ensure Panel extensions are loaded
pn.extension('perspective')

# List of available Seaborn datasets
datasets = sns.get_dataset_names()

class Dashboard:
    def __init__(self):
        self.df = sns.load_dataset('penguins')
        
        # Dropdown to select dataset
        self.dataset_selector = pn.widgets.Select(name='Select Dataset', options=datasets, value='penguins')
        self.dataset_selector.param.watch(self.update_dataset, 'value')
        
        # Use PerspectiveViewer for interactive table
        self.perspective_table = pn.pane.Perspective(self.df, plugin='datagrid', sizing_mode='stretch_both')

        self.layout = pn.Column(
            self.dataset_selector,
            self.perspective_table,
        )

    def update_dataset(self, event):
        selected_dataset = event.new
        self.df = sns.load_dataset(selected_dataset)
        self.perspective_table.object = self.df
        self.perspective_table.name = selected_dataset.capitalize()

    def filter_table(self, event):
        filtered_df = self.df
        if self.day_filter.value != 'All':
            filtered_df = filtered_df[filtered_df['day'] == self.day_filter.value]
        if self.time_filter.value != 'All':
            filtered_df = filtered_df[filtered_df['time'] == self.time_filter.value]
        if self.gender_filter.value != 'All':
            filtered_df = filtered_df[filtered_df['sex'] == self.gender_filter.value]
        self.perspective_table.update(data=filtered_df)
        self.summary.object = self.generate_summary(filtered_df)
        self.plot.object = self.create_plot(filtered_df)

    def generate_summary(self, df=None):
        if df is None:
            df = self.df
        summary = df.describe().to_markdown()
        return f"## Summary Statistics\n{summary}"

    def create_plot(self, df=None):
        if df is None:
            df = self.df
        plot = df.hvplot.scatter(x='total_bill', y='tip', by='sex', size='size', hover_cols=['day', 'time'], title='Total Bill vs Tip by Gender')
        return pn.pane.HoloViews(plot)

app_instance = Dashboard()

app = pn.template.BootstrapTemplate(
    title="Template Interactive Dashboard App with Perspective",
    main=[app_instance.layout],
)

app.servable()

if __name__ == "__main__":
    # Serve the app on a local Panel server
    pn.serve(app, port=5006)  # You can specify the port if needed
