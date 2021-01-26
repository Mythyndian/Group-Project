import React from 'react';
import  ReactDOM from "react-dom";
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import '../../static/css/style.css';

const useStyles = makeStyles((theme) => ({
    container: {
      display: 'flex',
      flexWrap: 'wrap',
    },
    textField: {
      marginLeft: theme.spacing(1),
      marginRight: theme.spacing(1),
    },
  }));

  export default function DatePickers() {
    const classes = useStyles();
  
    return (
        <form className={classes.container} noValidate>
            <TextField
            id="date"
            label="Pick date"
            type="date"
            defaultValue="2017-05-24"
            className={classes.textField}
            InputLabelProps={{
                shrink: true,
            }}
            />
        </form>
    );
  }
  ReactDOM.render(
    DatePickers,
    document.getElementById('app')
  );
  /*export default class DatePicker extends Component {
    classes = useStyles();
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <form className={classes.container} noValidate>
              <TextField
                id="date"
                label="Birthday"
                type="date"
                defaultValue="2017-05-24"
                className={classes.textField}
                InputLabelProps={{
                  shrink: true,
                }}
              />
            </form>
          );
        }
    }
*/