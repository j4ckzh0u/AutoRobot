// import styles from './index.css';

// export default function() {
//   return (
//     <div className={styles.normal}>
//       <div className={styles.welcome} />
//       <ul className={styles.list}>
//         <li>To get started, edit <code>src/pages/index.js</code> and save to reload.</li>
//         <li><a href="https://umijs.org/guide/getting-started.html">Getting Started</a></li>
//       </ul>
//     </div>
//   );
// }


import React, { PureComponent } from 'react'
import Redirect from 'umi/redirect'
import { withI18n } from '@lingui/react'

@withI18n()
class Index extends PureComponent {
  render() {
    const { i18n } = this.props
    // return <Redirect to={i18n.t`/dashboard`} />
    return <Redirect to={`/dashboard`} />
  }
}

export default Index
